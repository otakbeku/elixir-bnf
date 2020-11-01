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

```
<elixir_program>
```

### Program -> Expression List
```
<expression_list>
```

### Expression List -> Expression
```
<expression>

<expression_list>
```

# Module Definition

### Expression -> Module Definition
```
<module_definition>

<expression_list>
```

### module_definition -> defmodule <nested_alias> do <module_body> end
```
defmodule <nested_alias> do 
    <module_body> 
end

<expression_list>
```

### <nested_alias> -> <alias>
```
defmodule <alias> do 
    <module_body> 
end

<expression_list>
```

### <alias> -> <alpha_upper><alias_term_list>
```
defmodule <alpha_upper><alias_term_list> do 
    <module_body> 
end

<expression_list>
```

### <alpha_upper> -> C
```
defmodule C<alias_term_list> do 
    <module_body> 
end

<expression_list>
```

### <alias_term_list> -> <alpha_num><alias_term_list>
```
defmodule C<alpha_num><alias_term_list> do 
    <module_body> 
end

<expression_list>
```

### <alpha_num> -> <alpha>
```
defmodule C<alpha><alias_term_list> do 
    <module_body> 
end

<expression_list>
```

### <alpha> -> <alpha_lower>
```
defmodule C<alpha_lower><alias_term_list> do 
    <module_body> 
end

<expression_list>
```

### <alpha_lower> -> o
```
defmodule Co<alias_term_list> do 
    <module_body> 
end

<expression_list>
```

### Ulangi 4 step sebelum ini untuk menulis sisa <alpha_num> menjadi `ntoh<alpha_num>`

```
defmodule Contoh<alpha_num> do 
    <module_body> 
end

<expression_list>
```

### <alpha_num> -> <decimal>

```
defmodule Contoh<decimal> do 
    <module_body> 
end

<expression_list>
```

### <decimal> -> 2

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

### <module_specifix_expr> -> <named_function_def>
```
defmodule Contoh2 do 
    <named_function_def>
    <module_body>
end

<expression_list>
```

### <named_function_def> -> <def_token> <function_head> <do_block>
```
defmodule Contoh2 do 
    <def_token> <function_head> <do_block>
    <module_body>
end

<expression_list>
```

### <def_token> -> def
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

### <identifier_start> -> <alpha_lower>
```
defmodule Contoh2 do 
    def <alpha_lower><identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <alpha_lower> -> i
```
defmodule Contoh2 do 
    def i<identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <identifier_continue> -> <alpha_num><identifier_continue>
```
defmodule Contoh2 do 
    def i<alpha_num><identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <alpha_num> -> <alpha>
```
defmodule Contoh2 do 
    def i<alpha><identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <alpha> -> <alpha_lower>
```
defmodule Contoh2 do 
    def i<alpha_lower><identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <alpha_lower> -> s
```
defmodule Contoh2 do 
    def is<identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### Mengulang <identifier_continue> seperti sebelumnya, hingga <alpha><identifier_continue> 
```
defmodule Contoh2 do 
    def is<alpha><identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### <alpha> -> _
```
defmodule Contoh2 do 
    def is_<identifier_continue><identifier_end>(<parameter_list>) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```

### Mengulangi penurunan untuk <identifier_continue> hingga menjadi `is_prime_numbe<identifier_end>`
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
    def is_prime_number(a, b) when <guards_expr> <do_block>
    <module_body>
end

<expression_list>
```
