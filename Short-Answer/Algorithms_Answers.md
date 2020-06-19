#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity of this is O(n) because after the first run of the while loop a == n * n and increases by n * n after each time the loop runs. We can think of the final result as (nth run of the loop) n * n as == n * n * n. Therefore, the loop needs to run n times in order to stop executing. This runtime increases linearly as n increases linearly.

b) The runtime complexity is O(n log n). The for loop dealing with the variable i will run n times and therefore has a runtime complexity of O(n). The nested for loop dealing with the variable j has a runtime of O(log n) with log having a base of 2. This is because j starts as 1 and is doubled with each iteration of that loop, so therefore j will surpass the variable n after log n iterations (although if the answer is a float such as 2.5 then the number of loop iterations will be the next highest integer in this case 3). Therefore, if we multiply the runtime complexities of the two for loops we get an overall runtime complexity of O(n log n) with log having a base of 2.

c) The runtime complexity of the solution is O(n) because the function will always be called bunnies + 1 times. Therefore the number of executions increases linearly as bunnies increases linearly.

## Exercise II

1. Create the variables top_possible, lowest possible, current_floor,. Initialize top_possible to n, lowest possible to 1, and current_floor to top_possible + lowest_possible // 2
2. Create a while loop that always runs (while True:). Inside of it drop an egg from current floor. If it breaks then reassign top possible to current_floor. If the egg does not break, reassign lowest_possible to current_floor + 1.
3. After step 2 still inside of the while loop, create an if statement that returns lowest_possible if top_possible == lowest_possible. Otherwise the current_floor should be reassigned to top_possible + lowest_possible // 2  using the updated top_possible and lowest_possible values.

Answer: The runtime complexity of this solution is O(log n) with the log having a base of 2.