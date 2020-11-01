``` Elixir
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
```

## Program -> Expression List
```
<elixir_program>
```

```
<expression_list>
```
## Expression List -> Expression
```
<expression_list>
```

```
<expression>

<expression_list>
```

## Expression -> Module Definition
```
<expression>

<expression_list>
```

```
<module_definition>

<expression_list>
```

## Module_definition expand

```
<module_definition>

<expression_list>
```

```
defmodule <nested_alias> do 
    <module_body> 
end

<expression_list>
```

