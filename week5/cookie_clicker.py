"""
Cookie Clicker Simulator
2016-Feb-09
Python 2.7
Chris
"""



# Used to increase the timeout, if necessary
#import simpleplot
#import codeskulptor
#codeskulptor.set_timeout(20)

import logging
import math
import poc_clicker_provided as provided
from matplotlib import pyplot as plt

# Constants
SIM_TIME = 10000000000.0
#SIM_TIME = 100.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._total_cookies_produced = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0
        self._game_history = [(0.0, None, 0.0, 0.0)] # time, item bought, cost of item, total cookies produced

    def __str__(self):
        """
        Return human readable state
        """
        return ' Total Cookies Produced %r \n Current Cookies %r \n Current Time %r \n \
Current CPS %r' % (self._total_cookies_produced, self._current_cookies, \
            self._current_time, self._current_cps)

    def get_total_cookies(self):
        """
        Return total cookies produced
        (not current cookies in hand)
        """
        return self._total_cookies_produced

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self._current_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._game_history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        time_left = (cookies - self._current_cookies) / float(self._current_cps)
        return max(0.0, math.ceil(time_left))

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self._current_time += time
            self._current_cookies += (time * self._current_cps)
            self._total_cookies_produced += (time * self._current_cps)


    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies < cost:
            return
        else:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._game_history.append((self._current_time, item_name, cost, self._total_cookies_produced))


def simulate_clicker(build_info, duration, strategy, discount_value = 1.0):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    # Replace with your code

    my_state = ClickerState()
    my_build_info = build_info.clone()

    while my_state.get_time() <= duration:

        next_item = strategy(my_state.get_cookies(), my_state.get_cps(), \
        my_state.get_history(), (duration - my_state.get_time()), my_build_info, discount_value)

        if next_item == None:
            break

        until_next_item = my_state.time_until(my_build_info.get_cost(next_item))

        if until_next_item + my_state.get_time() > duration:
            break

        my_state.wait(until_next_item)
        my_state.buy_item(next_item, my_build_info.get_cost(next_item), my_build_info.get_cps(next_item))
        my_build_info.update_item(next_item)

    if my_state.get_time() <= duration:
        time_left = duration - my_state.get_time()
        my_state.wait(time_left)
        my_state.buy_item('End', 0.0, 0.0) #add final score to history - remove for owltest

    print my_state.get_total_cookies()

    logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG, format='%(message)s')
    logging.debug(str(my_state.get_total_cookies()) + ',' + str(discount_value))

    return my_state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info, discount_value):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info, discount_value):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info, discount_value):
    """
    Always buy the cheapest item you can afford in the time left.
    """

    names_items = build_info.build_items()
    cheapest_item = float('inf')
    cheapest_item_name = None
    for item in names_items:
        if build_info.get_cost(item) < cheapest_item and (cookies + (cps * time_left)) >= build_info.get_cost(item):
            cheapest_item = build_info.get_cost(item)
            cheapest_item_name = item

    return cheapest_item_name

def strategy_expensive(cookies, cps, history, time_left, build_info, discount_value):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    names_items = build_info.build_items()
    expensive_item = 0
    expensive_item_name = None
    for item in names_items:
        if build_info.get_cost(item) > expensive_item and (cookies + (cps * time_left)) >= build_info.get_cost(item):
            expensive_item = build_info.get_cost(item)
            expensive_item_name = item

    return expensive_item_name

def strategy_best(cookies, cps, history, time_left, build_info, discount_value):
    """
    The best strategy that you are able to implement.
    """
    # potential strategies to maximise strategy:
    # logging build order purchases
    # time value of money
    # monte carlo end (basic strat to start, but monte carlo end as that is key)

    # cost / current CPS + cost / delta CPS
    if time_left > SIM_TIME / 2.0:
        discount_value -= 0.041
    elif time_left > SIM_TIME / 8.0:
        discount_value -= 0.051

    #logging.basicConfig(filename='log2_filename.txt', level=logging.DEBUG, format='%(message)s')
    names_items = build_info.build_items()
    best_ratio = 0.0
    best_ratio_name = None
    for item in names_items:
        eff = build_info.get_cps(item) / float(build_info.get_cost(item) ** discount_value)
        #logging.debug(discount_value, ',', str(eff))
        if eff > best_ratio and (cookies + (cps * time_left)) >= build_info.get_cost(item):
            best_ratio = eff
            best_ratio_name = item
    return best_ratio_name


def test_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    # Replace with your code

    my_test_state = ClickerState()
    my_test_build_info = build_info.clone()

    while my_test_state.get_time() <= duration:

        next_item = strategy

        until_next_item = my_test_state.time_until(my_test_build_info.get_cost(next_item))

        if until_next_item + my_test_state.get_time() > duration:
            break

        my_test_state.wait(until_next_item)
        my_test_state.buy_item(next_item, my_test_build_info.get_cost(next_item), my_test_build_info.get_cps(next_item))
        my_test_build_info.update_item(next_item)

    if my_test_state.get_time() <= duration:
        time_left = duration - my_test_state.get_time()
        my_test_state.wait(time_left)
        my_test_state.buy_item('End', 0.0, 0.0) #add final score to history

    dict_data = {'total': my_test_state.get_total_cookies(), 'cookies': my_test_state.get_cookies(), 'cps': my_test_state.get_cps(), 'time': my_test_state.get_time()}
    return (dict_data, my_test_build_info)

def run_strategy(strategy_name, time, strategy, discount_value = 1.0):
    """
    Run a simulation for the given time with one strategy.
    """
    my_graph_history = []
    state = simulate_clicker(provided.BuildInfo(), time, strategy, discount_value)
    my_history = state.get_history()
    my_graph_history = [(item[0], item[3]) for item in my_history]
    print strategy_name, ":", state
    return my_graph_history

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)


'''for x in range(1, 100):
    run_strategy("Test", SIM_TIME, strategy_test, (x/float(100))+1)'''

'''for x in range(4250000, 4399999):
    print (x/float(100000000)) + 1
'''
# keep above

def run():
    """
    Run the simulator.
    """
    cursor_graph = run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    cheap_graph = run_strategy("Cheap", SIM_TIME, strategy_cheap)
    expensive_graph = run_strategy("Expensive", SIM_TIME, strategy_expensive)

    cursor_graph_x, cursor_graph_y = zip(*cursor_graph)
    cheap_graph_x, cheap_graph_y = zip(*cheap_graph)
    expensive_graph_x, expensive_graph_y = zip(*expensive_graph)

    plt.loglog(cursor_graph_x, cursor_graph_y, lw=2, label='Cursor')
    plt.loglog(cheap_graph_x, cheap_graph_y, lw=2, label='Cheap')
    plt.loglog(expensive_graph_x, expensive_graph_y, lw=2, label='Expensive')

    best_graph = run_strategy("Best", SIM_TIME, strategy_best, 1.04393) # 1.34019 x 10^18   # 1.04 to 1.06 multiplier is best
    best_graph_x, best_graph_y = zip(*best_graph)
    plt.loglog(best_graph_x, best_graph_y, lw=2, label='Best')

    plt.title('Cookie Clicker - Strategy Comparisons')
    plt.xlabel('Time')
    plt.ylabel('Total Cookies')

    plt.legend(loc='upper left')
    plt.show()

#run_strategy("Best", SIM_TIME, strategy_best, 1.04393)
run()
