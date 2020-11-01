defmodule Contoh2 do
  def is_prime_number(a, i) when i<a/2 and rem(a, i) != 0  do
    IO.puts("#{a} is prime number")
    end
  def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0do
    IO.puts("#{a} is not prime number")
    end
  def find_prime(a) do
      k = 1
      is_prime_number(a, k+1)
  end
end

Contoh2.find_prime(10)
