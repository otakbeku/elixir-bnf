contoh3_code = """
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
"""

terminals3 = ["defmodule","alias_name","do","def", "funct_name", "(", ")", "param_name", ",", "var_name", "=", "[", "]", "number", "end", ".", "|", "_", "+", "-"]

symbols3 = [
  "defmodule", "alias_name", "do", 
    "def", "funct_name", "(","param_name", ")", "do", 
      "var_name", "=", "[","number", ",", "number", "]", 
      "funct_name", "(", "var_name", ",", "var_name", ")",
    "end",
    "def", "funct_name", "(", "param_name", ",", "number", ")", "do",
      "alias_name", ".", "funct_name", "(","var_name", ")",
    "end",
    "def", "funct_name", "(", "param_name", ",", "param_name", ")", "do",
      "[","var_name", ",", "var_name", "|", "_", "]", "=", "var_name",
      "funct_name", "(","[","var_name", "+", "var_name", "|", "var_name", "]", ",", "var_name", "-", "number", ")",
    "end",
  "end",
  "alias_name",".","funct_name", "(", "funct_name", "(", "alias_name", ".", "funct_name", "(", "number", ")", ")", ")", "EOF"]

contoh3 = [contoh3_code, terminals3, symbols3]

# asignment, list, patern matching, or and empty, 

contoh2_code = """
defmodule Contoh2 do
  def is_prime_number(a, i) when i<a/2 and rem(a, i) != 0  do
    IO.puts("#{a} is prime number")
    end
  def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
    IO.puts("#{a} is not prime number")
    end
  def find_prime(a) do
      k = 1
      is_prime_number(a, k+1)
  end
end

Contoh2.find_prime(10)
"""

terminals2 = ["defmodule","alias_name","do","def", "funct_name", "(", ")", "parameter", ",", "when","and", "<", "/", "!=", "==", "literal",'"', "#", "{", "}", "var_name", "=", "[", "]", "number", "end", ".", "|", "_", "+", "-"]

symbols2 = [
  "defmodule", "alias_name", "do", 
    "def", "funct_name", "(","param_name", ",", "param_name", ")", 
      "when", "var_name", "<","var_name","/", "number", 
      "and", "funct_name","(","var_name", ",", "var_name", ")", "!=", "number", "do", 
        "alias_name", ".", "funct_name", "(",'"',"#","{", "var_name" ,"}", "literal", "literal", "literal", '"', ")" ,
        "end",
    "def", "funct_name", "(","param_name", ",", "param_name", ")", 
      "when", "var_name", "<","var_name","/", "number", 
      "and", "funct_name","(","var_name", ",", "var_name", ")", "==", "number", "do", 
        "alias_name", ".", "funct_name", "(",'"',"#","{", "var_name" ,"}", "literal", "literal", "literal", "literal", '"', ")" ,
        "end",
    "def", "funct_name", "(","param_name", ")", "do",
      "var_name", "=", "number",
      "funct_name", "(", "var_name", ",", "var_name", "+", "number", ")",
    "end",
  "end", 
  "alias_name", ".", "funct_name", "(", "number", ")", "EOF"]


contoh2 = [contoh2_code, terminals2, symbols2]
# parameter list, binary operation (arith and comparison), string interpolation, pattern matching, when in function def


contoh1_code = """
defmodule Contoh1 do
  def hello do
    IO.puts("Hello world!")
  end
end

Contoh1.hello()
"""

# Lexxers :
# code : str -> terminal : list[str]

terminals1 = ["defmodule","alias_name","do","def","funct_name",".","(",r'"',r"'", ")", "end", "literal"]

symbols1 = ["defmodule","alias_name","do","def","funct_name","do", "alias_name",".","funct_name","(",'"',"literal","literal",'"',")","end","end", "alias_name", ".", "funct_name", "(", ")", "EOF"]

contoh1 = [contoh1_code, terminals1, symbols1]