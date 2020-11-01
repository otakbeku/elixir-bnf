``` Elixir
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

### <alias_term_list> -> <alpha_num><alias_term_list> -> <alpha><alias_term_list> -> <alpha_lower><alias_term_list> -> o<alias_term_list>
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

### <alias_term_list> -> <alpha_num> -> <decimal> -> <decimal_digit> -> 2
```
defmodule Contoh2 do 
    <module_body> 
end

<expression_list>
```
# Function Definition 1

### <module_body> -> <module_specifix_expr><module_body>
```
defmodule Contoh2 do 
    <module_specifix_expr>
    <module_body>
end

<expression_list>
```

### <module_specifix_expr> -> <named_function_def> -> <def_token> <function_head> <do_block> -> def <function_head> <do_block>
```
defmodule Contoh2 do 
    def <function_head> <do_block>
    <module_body>
end

<expression_list>
```

### <function head> -> <function_name>(<parameter_list>) when <guards_expr>
```
defmodule Contoh2 do 
    def <function_name>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <function_name> -> <identifier_name>
```
defmodule Contoh2 do 
    def <identifier_name>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

## Identifier Name

### <identifier_name> -> <identifier_start><identifier_continue><identifier_end>
```
defmodule Contoh2 do 
    def <identifier_start><identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <identifier_start> -> <alpha_lower> -> i
```
defmodule Contoh2 do 
    def i<identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <identifier_continue> -> <alpha_num><identifier_continue> -> <alpha><identifier_continue> -> <alpha_lower><identifier_continue> -> s<identifier_continue>
```
defmodule Contoh2 do 
    def is<identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <identifier_continue> -> <alpha_num><identifier_continue> -> <alpha><identifier_continue> -> _<identifier_continue>
```
defmodule Contoh2 do 
    def is_<identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### Mengulangi penurunan untuk <identifier_continue> hingga menjadi `is_prime_numb<identifier_continue><identifier_end>`
```
defmodule Contoh2 do 
    def is_prime_numb<identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <identifier_continue> -> <alpha_num> -> <alpha> -> <alpha_lower> -> e
```
defmodule Contoh2 do 
    def is_prime_numbe<identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <identifier_end> -> <alpha_num> -> <alpha> -> <alpha_lower> -> r
```
defmodule Contoh2 do 
    def is_prime_number(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

## Parameter List

### <parameter_list> -> <parameter>, <parameter_list>
```
defmodule Contoh2 do 
    def is_prime_number(<parameter>, <parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <parameter> -> <parameter_name> -> <identifier_name> -> <identifier_start> -> a
```
defmodule Contoh2 do 
    def is_prime_number(a, <parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <parameter_list> -> <parameter> -> <parameter_name> -> <identifier_name> -> <identifier_start> -> b
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

## Guards

### <guards_expr> -> <strict_boolean_expr> -> <strict_boolean_expr> <strict_boolean_operator> <term>
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when <strict_boolean_expr> <strict_boolean_operator> <term> <do_block>
    <module_body>
end

<expression_list>
```

### <strict_boolean_expr> -> <boolean> -> <comparison_expr> -> <comparison_expr> <comparison_operator> <comparison_expr>
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when <comparison_expr> <comparison_operator> <comparison_expr> <strict_boolean_operator> <term> <do_block>
    <module_body>
end

<expression_list>
```

### <comparison_expr> -> <identifier_name> -> <identifier_start> -> i
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i <comparison_operator> <comparison_expr> <strict_boolean_operator> <term> <do_block>
    <module_body>
end

<expression_list>
```

### <comparison_operator> -> <
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < <comparison_expr> <strict_boolean_operator> <term> <do_block>
    <module_body>
end

<expression_list>
```

### <comparison_expr> -> <expression> -> <arithmatic_expr> -> <arithmetic_expr> <arithmetic_operator> <arithmetic_expr>
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < <arithmetic_expr> <arithmetic_operator> <arithmetic_expr> <strict_boolean_operator> <term> <do_block>
    <module_body>
end

<expression_list>
```

### <arithmetic_expr> -> <identifier_name> -> <identifier_start> -> a
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a <arithmetic_operator> <arithmetic_expr> <strict_boolean_operator> <term> <do_block>
    <module_body>
end

<expression_list>
```

### <arithmetic_operator> -> /
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / <arithmetic_expr> <strict_boolean_operator> <term> <do_block>
    <module_body>
end

<expression_list>
```

### <arithmetic_expr> -> <number> -> <integer> -> <non_neg_integer> -> <decimal> -> <decimal_digit> -> 2
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 <strict_boolean_operator> <term> <do_block>
    <module_body>
end

<expression_list>
```

### <strict_boolean_operator> -> and
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and <term> <do_block>
    <module_body>
end

<expression_list>
```

### <term> -> <boolean> -> <comparison_expr> -> <comparison_expr> <comparison_operator> <comparison_expr>
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and <comparison_expr> <comparison_operator> <comparison_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <comparison_expr> -> <expression> -> <function_call> -> <non_qualified_function_call><arg_term> -> <function_name><arg_term> -> <identifier_name><arg_term> -> <identifier_name>(<arg_list>)
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and <identifier_name>(<arg_list>) <comparison_operator> <comparison_expr> <do_block>
    <module_body>
end

<expression_list>
```

### dengan penurunan identifier name yang telah dilakukan sebelumnya (identifier name bisa diturunkan menjadi urutan alphanumeric apapun)
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(<arg_list>) <comparison_operator> <comparison_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <arg_lsit> -> <arg>, <arg_list> -> <arg>, <arg>
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(<arg>, <arg>) <comparison_operator> <comparison_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <arg> -> <variable_name> -> <identifier_name> -> <identifier_start> -> <alpha_lower> -> a
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, <arg>) <comparison_operator> <comparison_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <arg> -> <variable_name> -> <identifier_name> -> <identifier_start> -> <alpha_lower> -> i
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) <comparison_operator> <comparison_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <comparison_operator> -> !=
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != <comparison_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <comparison_expr> -> <term> -> <integer> -> <non_neg_integer> -> <decimal> -> <decimal_digit> -> 0
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 <do_block>
    <module_body>
end

<expression_list>
```

### <do_block> -> do <expression_list> end -> do <expression> end -> do <function_call> end -> do <nested_alias>.<qualified_function_call><arg_term> end
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        <nested_alias>.<qualified_function_call><arg_term> 
    end
    <module_body>
end

<expression_list>
```

### <nested_alias> -> <alias> -> <alpha_upper><alias_term_list> -> I<alias_term_list> -> I<alpha_num> -> I<alpha>  -> I<alpha_upper> -> IO
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.<qualified_function_call><arg_term> 
    end
    <module_body>
end

<expression_list>
```

### <qualified_function_call> -> <function_name> -> <identifier_name> -> <identifier_start><identifier_continue><identifier_end>
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.<identifier_start><identifier_continue><identifier_end><arg_term>
    end
    <module_body>
end

<expression_list>
```

### Dengan mengikuti penurunan identifier name seperti sebelumnya, rangkaian alphabet huruf kecil bisa dicapai, sehingga <identifier_name> bisa menjadi `puts`
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts<arg_term>
    end
    <module_body>
end

<expression_list>
```

### <arg_term> -> (<arg_list>) -> (<arg>) -> (<term>) -> (<string>) -> ("<string_term_list>")
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("<string_term_list>")
    end
    <module_body>
end

<expression_list>
```

### <string_term_list> -> <string_term><string_term_list> -> <string_interpolation><string_term_list> -> #{ <expression> }<string_term_list> -> #{ <variable_name> }<string_term_list> -> 
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ <variable_name> }<string_term_list>")
    end
    <module_body>
end

<expression_list>
```

### <variable_name> -> <identifier_name> -> <identifier_start> -> <alpha_lower> -> a
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a }<string_term_list>")
    end
    <module_body>
end

<expression_list>
```

### <string_term_list> -> <string_term><string_term_list> -> <string_term_vanilla><string_term_list> -> <alpha><string_term_list> -> <alpha_lower><string_term_list> -> i<string_term_list>
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a }i<string_term_list>")
    end
    <module_body>
end

<expression_list>
```

### ulangi step yang sama untuk mendapatkan urutan simbol ` is prime numbe<string_term_list>`
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime numbe<string_term_list>")
    end
    <module_body>
end

<expression_list>
```

### <string_term_list> -> <string_term> -> <string_term_vanilla> -> <alpha> -> <alpha_lower> -> r
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    <module_body>
end

<expression_list>
```

# Function Definition 2

lakukan proses yang sama untuk menurunkan <module_body> menjadi function definition dan module body lainnya, sehingga didapatkan seperti berikut

```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) <comparison_operator> <comparison_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <comparison_operator> -> ==
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) == <comparison_expr> <do_block>
    <module_body>
end

<expression_list>
```

lalu lanjutkan penurunan yang sama seperti function definition 1 hingga selesai
### penurunan definisi fungsi 2
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    <module_body>
end

<expression_list>
```

# Function Definition 3

### <module_body> -> <module_specifix_expr> -> <named_function_def> -> <def_token> <function_head> <do_block> -> def <function_head> <do_block> -> def <function_name>(<parameter_list>) <do_block>
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def <function_name>(<parameter_list>) <do_block>
end

<expression_list>
```

### lakukan proses yang sama untuk menurunkan <function_name> menjadi `find_prime` 

```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(<parameter_list>) <do_block>
end

<expression_list>
```

### <parameter_list> -> <parameter> -> <parameter_name> -> <identifier_name> -> <identifier_start> -> <alpha_lower> -> a

```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) <do_block>
end

<expression_list>
```

### <do_block> -> do <expression_list> end -> do <expression><expression_list> end -> do <expression><expression> end 

```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
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
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
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
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
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
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
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
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        is_prime_number(<arg_list>)
    end 
end

<expression_list>
```

### <arg_list> -> <arg>,<arg_list> -> <expression>,<arg_list> -> <variable_name>,<arg_list> -> <identifier_name>,<arg_list> -> <identifier_start>,<arg_list> -> <alpha_lower>,<arg_list> -> a,<arg_list>
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        is_prime_number(a,<arg_list>)
    end 
end

<expression_list>
```

### <arg_list> -> <arg> -> <expression> -> <arithmetic_expr> -> <arithmetic_expr> <arithmetic_operator> <arithmetic_expr>
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        is_prime_number(a,<arithmetic_expr> <arithmetic_operator> <arithmetic_expr>)
    end 
end

<expression_list>
```

### <arithmetic_expr> -> <expression> -> <variable_name> -> <identifier_name> -> <identifier_start> -> <alpha_lower> -> k
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        is_prime_number(a,k <arithmetic_operator> <arithmetic_expr>)
    end 
end

<expression_list>
```

### <arithmetic_operator> -> +
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        is_prime_number(a,k + <arithmetic_expr>)
    end 
end

<expression_list>
```

### <arithmetic_expr> -> <expression> -> <term> -> <integer> -> <non_neg_integer> -> <decimal> -> <decimal_digit> -> 1
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        is_prime_number(a,k + 1)
    end 
end

<expression_list>
```

# Function Call

### <expression_list> -> <expression> -> <named_function_call> -> <nested_alias>.<qualified_function_call><arg_term> -> <alias>.<qualified_function_call><arg_term>
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        is_prime_number(a,k + 1)
    end 
end

<alias>.<qualified_function_call><arg_term>
```

### Gunakan penurunan alias pada definisi modul untuk mengubah <alias> menjadi `Contoh2`
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        is_prime_number(a,k + 1)
    end 
end

Contoh2.<qualified_function_call><arg_term>
```

### <qualified_function_call> -> <function_name> -> <identifier_name>
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        is_prime_number(a,k + 1)
    end 
end

Contoh2.<identifier_name><arg_term>
```

### Gunakan penurunan <identifier_name> seperti Definisi Fungsi 3 untuk mengubah <identifier_name> menjadi `find_prime`
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        is_prime_number(a,k + 1)
    end 
end

Contoh2.find_prime<arg_term>
```

### <arg_term> -> (<arg_list>) -> (<arg>) -> (<expression>) -> (<term>) -> (<integer>) -> (<non_neg_integer>) -> (<decimal>) -> (<decimal_digit><decimal>) -> (1<decimal>) -> (1<decimal_digit>) -> (10)
```
defmodule Contoh2 do 
    def is_prime_number(a, i) when i < a / 2 and rem(a, i) != 0 do 
        IO.puts("#{ a } is prime number")
    end
    def is_prime_number(a, i) when i<a/2 and rem(a, i) == 0 do
        IO.puts("#{ a } is not prime number")
    end
    def find_prime(a) do 
        k = 1
        is_prime_number(a,k + 1)
    end 
end

Contoh2.find_prime(10)
```



