defmodule Contoh3 do
  def find_fibonacci(nth) do
    list = [1, 1]
    fib(list, nth)
  end

  def fib(list, 2) do
    Enum.reverse(list)
  end

  def fib(list, n) do
    [first_elem, second_elem | _] = list
    fib([first_elem + second_elem | list], n - 1)
  end
end

IO.puts(inspect(Contoh3.find_fibonacci(10)))
