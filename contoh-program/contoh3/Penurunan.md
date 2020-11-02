``` Elixir
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

```

# Expression List
### Simbol Awal
```
<expression_list>
```

### <expression_list> -> <expression> <expression_list>
```
<expression>

<expression_list>
```

# Module Definition

### <expression> -> <module_definition> -> defmodule <nested_alias> do <module_body> end
```
<module_definition>

<expression_list>
```

### <nested_alias> -> <alias> -> <alpha_upper><alias_term_list> -> C<alias_term_list>
```
defmodule C<alias_term_list> do 
    <module_body> 
end

<expression_list>
```

### <alias_term_list> -> <alphanum><alias_term_list> -> <alpha><alias_term_list> -> <alpha_lower><alias_term_list> -> o<alias_term_list>
```
defmodule Co<alias_term_list> do 
    <module_body> 
end

<expression_list>
```

### Ulangi step sebelum ini untuk menulis sisa <alias_term_list> menjadi `ntoh<alias_term_list>`

```
defmodule Contoh<alias_term_list> do 
    <module_body> 
end

<expression_list>
```

### <alias_term_list> -> <alphanum> -> <decimal> -> <decimal_digit> -> 3
```
defmodule Contoh3 do 
    <module_body> 
end

<expression_list>
```
# Function Definition 1

### <module_body> -> <module_specific_expr><module_body>
```
defmodule Contoh3 do 
    <module_specific_expr>
    <module_body>
end

<expression_list>
```

### <module_specific_expr> -> <named_function_def> -> <def_token> <function_head> <do_block> -> def <function_head> <do_block>
```
defmodule Contoh3 do 
    def <function_head> <do_block>
    <module_body>
end

<expression_list>
```

### <function head> -> <function_name>(<parameter_list>)
```
defmodule Contoh3 do 
    def <function_name>(<parameter_list>) <do_block>
    <module_body>
end

<expression_list>
```

### <function_name> -> <identifier_name>
```
defmodule Contoh3 do 
    def <identifier_name>(<parameter_list>) <do_block>
    <module_body>
end

<expression_list>
```

## Identifier Name

### <identifier_name> -> <identifier_start><identifier_continue><identifier_end>
```
defmodule Contoh3 do 
    def <identifier_start><identifier_continue><identifier_end>(<parameter_list>) <do_block>
    <module_body>
end

<expression_list>
```

### <identifier_start> -> <alpha_lower> -> f
```
defmodule Contoh3 do 
    def f<identifier_continue><identifier_end>(<parameter_list>) <do_block>
    <module_body>
end

<expression_list>
```

### <identifier_continue> -> <alphanum><identifier_continue> -> <alpha><identifier_continue> -> <alpha_lower><identifier_continue> -> i<identifier_continue>
```
defmodule Contoh3 do 
    def fi<identifier_continue><identifier_end>(<parameter_list>) <do_block>
    <module_body>
end

<expression_list>
```

### Mengulangi penurunan untuk <identifier_continue> hingga menjadi `find<identifier_continue><identifier_end>`
```
defmodule Contoh3 do 
    def find<identifier_continue><identifier_end>(<parameter_list>) <do_block>
    <module_body>
end

<expression_list>
```

### <identifier_continue> -> <alphanum><identifier_continue> -> <alpha><identifier_continue> -> _<identifier_continue>
```
defmodule Contoh3 do 
    def find_<identifier_continue><identifier_end>(<parameter_list>) <do_block>
    <module_body>
end

<expression_list>
```

### Mengulangi penurunan untuk <identifier_continue> hingga menjadi `find_fibonac<identifier_continue><identifier_end>`
```
defmodule Contoh3 do 
    def find_fibonac<identifier_continue><identifier_end>(<parameter_list>) <do_block>
    <module_body>
end

<expression_list>
```

### <identifier_continue> -> <alphanum> -> <alpha> -> <alpha_lower> -> c
```
defmodule Contoh3 do 
    def find_fibonacc<identifier_end>(<parameter_list>) <do_block>
    <module_body>
end

<expression_list>
```

### <identifier_end> -> <alphanum> -> <alpha> -> <alpha_lower> -> i
```
defmodule Contoh3 do 
    def find_fibonacci(<parameter_list>) <do_block>
    <module_body>
end

<expression_list>
```

## Parameter List

### <parameter_list> -> <parameter>
```
defmodule Contoh3 do 
    def find_fibonacci(<parameter>) <do_block>
    <module_body>
end

<expression_list>
```

### <parameter> -> <parameter_name> -> <identifier_name>
```
defmodule Contoh3 do 
    def find_fibonacci(<identifier_name>) <do_block>
    <module_body>
end

<expression_list>
```

### Dengan penurunan yang sama seperti nama fungsi (karena sama2 <identifier_name> dan hanya terdiri dari huruf kecil maka <identifier_name> dapat diturunkan menjadi `nth`
```
defmodule Contoh3 do 
    def find_fibonacci(nth) <do_block>
    <module_body>
end

<expression_list>
```
## Do Block

### <do_block> -> do <expression_list> end -> do <expression><expression_list> end -> do <assignment><expression_list> end -> do <variable_name> = <expression><expression_list> end -> do <identifier_name> = <expression><expression_list> end
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        <identifier_name> = <expression>
        <expression_list> 
    end
    <module_body>
end

<expression_list>
```

### dengan penurunan <identifier_name> seperti penurunan <function_name> maka bisa diturunkan menjadi `list`
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        list = <expression>
        <expression_list> 
    end
    <module_body>
end

<expression_list>
```

### <expression> -> <term> -> <list> -> [<list_element_array>] -> [<list_element>,<list_element_array>] -> [<term>,<list_element_array>] -> [<integer>,<list_element_array>] -> [<decimal>,<list_element_array>] -> [<decimal_digit>,<list_element_array>] -> [1,<list_element_array>]
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        list = [1,<list_element_array>]
        <expression_list> 
    end
    <module_body>
end

<expression_list>
```

### <list_element_array> -> <list_element> -> <term> -> <integer> -> <decimal> -> <decimal_digit> -> 1
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        list = [1,1]
        <expression_list> 
    end
    <module_body>
end

<expression_list>
```

### <expression_list> -> <expression> -> <function_call> -> <non_qualified_function_call><arg_term> -> <function_name><arg_term> -> <identifier_name><arg_term> -> <identifier_name>(<arg_list>)
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        list = [1,1]
        <identifier_name>(<arg_list>)
    end
    <module_body>
end

<expression_list>
```

### dengan menggunakan penurunan yang sama seperti untuk nama fungsi, <identifier_name> menjadi `fib`
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        list = [1,1]
        fib(<arg_list>)
    end
    <module_body>
end

<expression_list>
```

### <arg_list> -> <arg>,<arg_list> -> <expression>,<arg_list> -> <variable_name>,<arg_list> -> <identifier_name>,<arg_list> -> <identifier_name>,<variable_name> -> <identifier_name>,<identifier_name>
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        list = [1,1]
        fib(<identifier_name>, <identifier_name>)
    end
    <module_body>
end

<expression_list>
```

### dengan penurunan identifier name, bisa didapat
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        list = [1,1]
        fib(list, nth)
    end
    <module_body>
end

<expression_list>
```

# Function Definition 2
### ulangi penurunan module body sehingga menjadi function definition dengan nama dan parameter serta expression_list
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        list = [1,1]
        fib(list, nth)
    end
    def fib(list, 2) do
        <qualified_function_call><arg_term>
    end

    def fib(list, n) do
        <assignment>
        <non_qualified_function_call><arg_term>
    end
end

<expression_list>
```

### <string_term_list> -> <string_term> -> <string_term_vanilla> -> <alpha> -> <alpha_lower> -> r
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    <module_body>
end

<expression_list>
```

# Function Definition 2

lakukan proses yang sama untuk menurunkan <module_body> menjadi function definition dan module body lainnya, sehingga didapatkan seperti berikut

```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i < a / 2 and rem(nth) <comparison_operator> <comparison_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <comparison_operator> -> ==
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i < a / 2 and rem(nth) == <comparison_expr> <do_block>
    <module_body>
end

<expression_list>
```

lalu lanjutkan penurunan yang sama seperti function definition 1 hingga selesai
### penurunan definisi fungsi 2
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    <module_body>
end

<expression_list>
```

# Function Definition 3

### <module_body> -> <module_specific_expr> -> <named_function_def> -> <def_token> <function_head> <do_block> -> def <function_head> <do_block> -> def <function_name>(<parameter_list>) <do_block>
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def <function_name>(<parameter_list>) <do_block>
end

<expression_list>
```

### lakukan proses yang sama untuk menurunkan <function_name> menjadi `find_prime` 

```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(<parameter_list>) <do_block>
end

<expression_list>
```

### <parameter_list> -> <parameter> -> <parameter_name> -> <identifier_name> -> <identifier_start> -> <alpha_lower> -> a

```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) <do_block>
end

<expression_list>
```

### <do_block> -> do <expression_list> end -> do <expression><expression_list> end -> do <expression><expression> end 

```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        <expression>
        <expression> 
    end 
end

<expression_list>
```

### <expression> -> <assigment> -> <variable_name> = <expression> -> <identifier_name> = <expression> -> <identifier_start = <expression> -> <alpha_lower> = <expression> -> k = <expression>

```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = <expression>
        <expression> 
    end 
end

<expression_list>
```

### <expression> -> <term> -> <integer> -> <non_neg_integer> -> <decimal> -> <decimal_digit> -> 1
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        <expression> 
    end 
end

<expression_list>
```

### expression> -> <function_call> -> <non_qualified_function_call><arg_term> -> <function_name><arg_term> -> <identifier_name><arg_term> -> <identifier_name>(<arg_list>)
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        <identifier_name>(<arg_list>)
    end 
end

<expression_list>
```

### Penurunan <identifier_name> sama seperti untuk nama 2 fungsi pertama. Sehingga menjadi
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        find_fibonacci(<arg_list>)
    end 
end

<expression_list>
```

### <arg_list> -> <arg>,<arg_list> -> <expression>,<arg_list> -> <variable_name>,<arg_list> -> <identifier_name>,<arg_list> -> <identifier_start>,<arg_list> -> <alpha_lower>,<arg_list> -> a,<arg_list>
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        find_fibonacci(a,<arg_list>)
    end 
end

<expression_list>
```

### <arg_list> -> <arg> -> <expression> -> <arithmetic_expr> -> <arithmetic_expr> <arithmetic_operator> <arithmetic_expr>
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        find_fibonacci(a,<arithmetic_expr> <arithmetic_operator> <arithmetic_expr>)
    end 
end

<expression_list>
```

### <arithmetic_expr> -> <expression> -> <variable_name> -> <identifier_name> -> <identifier_start> -> <alpha_lower> -> k
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        find_fibonacci(a,k <arithmetic_operator> <arithmetic_expr>)
    end 
end

<expression_list>
```

### <arithmetic_operator> -> +
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        find_fibonacci(a,k + <arithmetic_expr>)
    end 
end

<expression_list>
```

### <arithmetic_expr> -> <expression> -> <term> -> <integer> -> <non_neg_integer> -> <decimal> -> <decimal_digit> -> 1
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        find_fibonacci(a,k + 1)
    end 
end

<expression_list>
```

# Function Call

### <expression_list> -> <expression> -> <named_function_call> -> <nested_alias>.<qualified_function_call><arg_term> -> <alias>.<qualified_function_call><arg_term>
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        find_fibonacci(a,k + 1)
    end 
end

<alias>.<qualified_function_call><arg_term>
```

### Gunakan penurunan alias pada definisi modul untuk mengubah <alias> menjadi `Contoh3`
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        find_fibonacci(a,k + 1)
    end 
end

Contoh3.<qualified_function_call><arg_term>
```

### <qualified_function_call> -> <function_name> -> <identifier_name>
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        find_fibonacci(a,k + 1)
    end 
end

Contoh3.<identifier_name><arg_term>
```

### Gunakan penurunan <identifier_name> seperti Definisi Fungsi 3 untuk mengubah <identifier_name> menjadi `find_prime`
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        find_fibonacci(a,k + 1)
    end 
end

Contoh3.find_prime<arg_term>
```

### <arg_term> -> (<arg_list>) -> (<arg>) -> (<expression>) -> (<term>) -> (<integer>) -> (<non_neg_integer>) -> (<decimal>) -> (<decimal_digit><decimal>) -> (1<decimal>) -> (1<decimal_digit>) -> (10)
```
defmodule Contoh3 do 
    def find_fibonacci(nth) do 
        IO.puts("#{ a } is prime number")
    end
    def find_fibonacci(nth) when i<a/2 and rem(nth) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        find_fibonacci(a,k + 1)
    end 
end

Contoh3.find_prime(10)
```



