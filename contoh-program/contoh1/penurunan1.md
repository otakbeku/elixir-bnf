defmodule Contoh1 do
  def hello do
    IO.puts("Hello world!")
  end
end

Contoh1.hello()

1. Start Symbol

	S

2. S -> <expression_list>

`<expression_list>`

3. <expression_list> -> <expression>; <expression_list>

```
<expression>
<expression_list>
```

4. <expression> -> <module_definition>

```
<module_definition>
<expression_list>
```
	
5. <module_definition> -> 	defmodule <nested_alias> do <module_body> end

```
defmodule <nested_alias> do 
	<module_body> 
end

<expression_list>
```
	
6. <nested_alias>  -> <alias>

```
defmodule <alias> do 
	<module_body> 
end
	
<expression_list>
```

7.1. <alias>  -> <alpha_upper><alias_term_list>

```
defmodule C<alias_term_list> do 
	<module_body> 
end
	
<expression_list>

```
7.2 <alias_term_list> -> <alpha_num><alias_term_list>

```
defmodule C<alpha_num><alias_term_list> do 
	<module_body> 
end
	
<expression_list>
```

7.3. <alpha_num> -> <alpha>

```
defmodule C<alpha><alias_term_list> do 
	<module_body> 
end

<expression_list>
```

7.4. <alpha> -> <alpha_lower>

```
defmodule C<alpha_lower><alias_term_list> do 
	<module_body> 
end
	
<expression_list>
```
	
7.5. <alpha_lower> -> o

```
defmodule Co<alias_term_list> do 
	<module_body> 
end
	
<expression_list>
```

7.5..x-2. ...

7.x-1. <alphanum> -> <decimal_digit>

```
defmodule Contoh<decimal_digit> do 
	<module_body> 
end

<expression_list>
```

7.x. <decimal_digit> -> 1

```
defmodule Contoh1 do 
	<module_body> 
end
	
<expression_list>
```
	
8. <module_body> -> <module_specific_expr>

```
defmodule Contoh1 do 
	<module_specific_expr>
end
	
<expression_list>
```
	
9. <module_specific_expr> -> <named_function_def>

```
defmodule Contoh1 do 
	<named_function_def>
end
	
<expression_list>
```
	
10. <named_function_def> ->	<def_token> <function_head> <do_block>
	
```
defmodule Contoh1 do 
	<def_token> <function_head> <do_block>
end
	
<expression_list>
```
	
11. <def_token> -> def 
	
```
defmodule Contoh1 do 
	def <function_head> <do_block>
end
	
<expression_list>
```

12. <function_head> -> <function_name>
	
```
defmodule Contoh1 do 
	def <function_name> <do_block>
end
	
<expression_list>
```

13. <function_name> -> <identifier_name>
	
```
defmodule Contoh1 do 
	def <identifier_name> <do_block>
end
	
<expression_list>
```
	
14.1. <identifier_name> -> <identifier_start><identifier_continue><identifier_end>
	
```
defmodule Contoh1 do 
	def <identifier_start><identifier_continue><identifier_end> <do_block>
end
	
<expression_list>
```
	
14.2. <identifier_start> -> <alpha_lower>

```
defmodule Contoh1 do 
	def <alpha_lower><identifier_continue><identifier_end> <do_block>
end
	
<expression_list>
```
	
14.3. <alpha_lower> -> h

```
defmodule Contoh1 do 
	def h<identifier_continue><identifier_end> <do_block>
end
	
<expression_list>
```
	
14.4. <identifier_continue> -> <alphanum><identifier_continue>

```
defmodule Contoh1 do 
	def h<alphanum><identifier_continue><identifier_end> <do_block>
end
	
<expression_list>
```

14.5..x-2. ...

14.x-1. <alphanum> -> <alpha_lower>

```
defmodule Contoh1 do 
	def hell<alpha_lower> <do_block>
end
	
<expression_list>
```

14.x. <alpha_lower> -> o

```
defmodule Contoh1 do 
	def hello <do_block>
end
	
<expression_list>
```
	
15. <do_block> -> do <expression_list> end

```
defmodule Contoh1 do 
	def hello do 
		<expression_list> 
	end
end
	
<expression_list>

```
16. <expression_list>  -> <function_call>

```
defmodule Contoh1 do 
	def hello do 
		<function_call> 
	end
end
	
<expression_list>
```
	
16. <function_call>  -> <nested_alias>.<qualified_function_name><arg_term>

```
defmodule Contoh1 do 
	def hello do 
		<nested_alias>.<qualified_function_name><arg_term>
	end
end
	
<expression_list>
```
	
17.1. <nested_alias> -> <alias>

```
defmodule Contoh1 do 
	def hello do 
		<alias>.<qualified_function_name><arg_term>
	end
end
	
<expression_list>
```
	
17.2. <alias>  -> <alpha_upper><alias_term_list>

	defmodule Contoh1 do 
		def hello do 
			<alpha_upper><alias_term_list>.<qualified_function_name><arg_term>
		end
	end
	
	<expression_list>
	
17.2..x-1. ...

17.x. <alpha_upper> -> O

```
defmodule Contoh1 do 
	def hello do 
		IO.<qualified_function_name><arg_term>
	end
end
	
<expression_list>
```
	
18. <qualified_function_name> -> <function_name>

```
defmodule Contoh1 do 
	def hello do 
		IO.<function_name><arg_term>
	end
end
	
<expression_list>
```
	
19.1. <function_name> -> <identifier_name>

```
defmodule Contoh1 do 
	def hello do 
		IO.<identifier_name><arg_term>
	end
end
	
<expression_list>
```
	
19.2..x-1. ...

19.x. <alpha_lower> -> s

```
defmodule Contoh1 do 
	def hello do 
		IO.puts <arg_term>
	end
end
	
<expression_list>
```

20. <arg_term> -> (<arg_list>)

```
defmodule Contoh1 do 
	def hello do 
		IO.puts (<arg_list>)
	end
end
	
<expression_list>
```

21. <arg_list> -> <arg>

```
defmodule Contoh1 do 
	def hello do 
		IO.puts (<arg>)
	end
end
	
<expression_list>
```

22. <arg> -> <expression>

```
defmodule Contoh1 do 
	def hello do 
		IO.puts (<expression>)
	end
end
	
<expression_list>
```

23. <expression> -> <term>

```
defmodule Contoh1 do 
	def hello do 
		IO.puts (<term>)
	end
end
	
<expression_list>
```

23. <term> -> <string>

```
defmodule Contoh1 do 
	def hello do 
		IO.puts (<string>)
	end
end
	
<expression_list>
```

24. <string> -> "<string_term_list>"

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("<string_term_list>")
	end
end

<expression_list>
```

25.1. <string_term_list> -> <string_term><string_term_list>

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("<string_term><string_term_list>")
	end
end
	
<expression_list>
```

25.2. <string_term> -> <string_term_vanilla>

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("<string_term_vanilla><string_term_list>")
	end
end
	
<expression_list>
```

25.3. <string_term_vanilla> -> <alpha>

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("<alpha><string_term_list>")
	end
end

<expression_list>
```

25.4..x-1.

25.x. <special_character> -> !

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("Hello world!")
	end
end

<expression_list>
```

26. <expression_list> -> <module_function_expression>

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("Hello world!")
	end
end

<module_function_expression>
```

27. <module_function_expression> -> <function_call>

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("Hello world!")
	end
end

<function_call>
```

27. <function_call>  -> <nested_alias>.<qualified_function_name><arg_term>

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("Hello world!")
	end
end

<nested_alias>.<qualified_function_name><arg_term>
```
	
27.1. <nested_alias>  -> <alias>

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("Hello world!")
	end
end

<alias>.<qualified_function_name><arg_term>
```
	
27.1..x-1. ...

27.x. <decimal_digit> -> 1

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("Hello world!")
	end
end

Contoh1.<qualified_function_name><arg_term>
```
	
28.1. <qualified_function_name> -> <function_name>

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("Hello world!")
	end
end

Contoh1.<function_name><arg_term>
```

28.2..x-1. ...

28.x. <alpha_lower> -> o

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("Hello world!")
	end
end

Contoh1.hello<arg_term>
```
	
29. <arg_term> -> ()

```
defmodule Contoh1 do 
	def hello do 
		IO.puts ("Hello world!")
	end
end

Contoh1.hello()
```
