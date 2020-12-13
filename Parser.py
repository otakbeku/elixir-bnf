import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

class ElixirParser():
    def __init__(self, symbols):
        self.i = 0
        self.symbols = symbols
        self.sym = symbols[self.i]
        self.comparison_operator = ['<', '>', '==', '!==', '!=', '==', '===', '>=', '<=']
        self.arithmetic_operator = ['+', '-', '*', '/']
        self.boolean_operator = ['and', 'or', "|", "&"]
        self.binary_operator_first = [
            *self.comparison_operator, *self.arithmetic_operator, *self.boolean_operator ]
        self.term_first = ["var_name", "number", '"', "[", "_", "alias_name", "funct_name"]

    def accept(self, term):
        if term != self.sym:
            raise Exception(
                f"Parsing Failed, {term} expected, get {self.sym} instead")
        print(f"Accepting {self.sym}")
        self.i += 1
        if self.i != len(self.symbols):
            self.sym = self.symbols[self.i]
        else:
            self.sym = None

    def parse(self):
        self.elixir_program()

# Production Rule

    def elixir_program(self):
        """
        <elixir_program> ::= <expression_list> EOF
        """
        logging.info("Calling elixir program")
        self.expression_list()
        self.accept("EOF")
        logging.info("Program Accepted")

    def assignment(self):
        """
        <assignment> ::= <term_extended> = <term_extended>

        TODO :
        - Ganti jadi <var_name> | <list_expr> = <term_extended>
        """
        logging.info('assignment')
        self.term_extended()
        self.accept("=")
        self.term_extended()
  
    def expression_list(self):
        """
        <expression_list> ::= <expression> <expression_prime>
        """
        logging.info("expression_list")
        self.expression()
        self.expression_prime()

    def expression(self):
        """
        <expression> ::= <module_definition>
            | <function_call>
            | <assignment> 
        """
        logging.info("expression")
        if self.sym == "defmodule":
            self.module_definition()
        elif self.sym in ["alias_name", "funct_name"]:
            self.function_call()
        elif self.sym in self.term_first:
            self.assignment()

    def expression_prime(self):
        """
        <expression_prime> ::= epsilon | <expression_list>
        """
        logging.info("expression_prime")
        if self.sym in ["defmodule", "alias_name", "var_name", "funct_name"]:
            self.expression_list()

    def module_definition(self):
        """
        <module_definition> ::= defmodule alias_name do <module_expression_list> end
        """
        logging.info("module_definition")
        self.accept("defmodule")
        self.accept("alias_name")
        self.accept("do")
        self.module_expression_list()
        self.accept("end")

    def module_expression_list(self):
        """
        <module_expression_list> ::= <module_expression><module_expression_prime>
        """
        logging.info("module_expression_list")
        self.module_expression()
        self.module_expression_prime()

    def module_expression(self):
        """
        <module_expression> ::= <function_definition> | <function_call>
        """
        logging.info("module_expression")
        if self.sym == "def":
            self.function_definition()
        if self.sym in ["alias_name", "funct_name"]:
            self.function_call()

    def module_expression_prime(self):
        """
        <module_expression_prime> ::= epsilon | <module_expression_list>
        """
        logging.info("module_expression_prime")
        if self.sym in ["def", "alias_name", "funct_name"]:
            self.module_expression_list()

    def function_definition(self):
        """
        <function_definition> ::= def function_name <function_head> do <expression_list> end  
        """
        logging.info("function_definition")
        self.accept("def")
        self.accept("funct_name")
        self.function_head()
        self.accept('do')
        self.expression_list()
        self.accept("end")

    def function_head(self):
        """
        <function_head> ::= epsilon
            | (<parameter_list>) <function_head_prime>
        """
        logging.info("function_head")
        if self.sym == "(":
            self.accept('(')
            self.parameter_list()
            self.accept(')')
            self.function_head_prime()
    
    def function_head_prime(self):
        """
        <function_head_prime> ::= epsilon 
            | when <term_extended>
        """
        logging.info("function_head_prime")
        if self.sym == 'when':
            self.accept('when')
            self.term_extended()

    def binary_operator(self):
        """
        <binary_operator> ::= 

        TODO :
        - ini list semua binary operator
        """
        logging.info("binary_operator")
        if self.sym in self.binary_operator_first:
            self.accept(self.sym)
        
    def binary_operation(self):
        """
        <binary_operation> ::= <binary_operator> <term> <binary_operation_prime>
        """
        logging.info("binary_operation")
        self.binary_operator()
        self.term()
        self.binary_operation_prime()

    def binary_operation_prime(self):
        """
        <binary_operation_prime> ::= epsilon | <binary_operation>
        """
        logging.info("binary_operation_prime")
        if self.sym in self.binary_operator_first:
            self.binary_operation()

    def list_expr(self):
        """
        <list_expr> ::= [ <term_ext_list> ]
        """
        self.accept('[')
        self.term_ext_list()
        self.accept(']')

    def term(self):
        """
        <term> ::= number
            | var_name
            | _
            | <string>
            | <list_expr>
            | <function_call>

        TODO :
        - Ini udah make sense belum kalau function call ada di term?
        """
        logging.info("term")
        
        if self.sym == "number":
            self.accept("number")
        elif self.sym == "var_name":
            self.accept("var_name")
        elif self.sym == "_":
            self.accept("_")
        elif self.sym == '"':
            self.string()
        elif self.sym == "[":
            self.list_expr()
        elif self.sym in ['funct_name', 'alias_name']:
            self.function_call()

    def term_extended(self):
        """
        <term_extended> ::= <term> <binary_operation_prime>
        """
        logging.info("term_extended")
        self.term()
        self.binary_operation_prime()

    def term_ext_list(self):
        """
        <term_ext_list> ::= <term_extended> <term_ext_prime>
        """
        logging.info("term_ext_list")
        self.term_extended()
        self.term_ext_prime()

    def term_ext_prime(self):
        """
        <term_ext_prime> ::= epsilon | , <term_ext_list>
        """
        logging.info("term_ext_prime")
        if self.sym == ",":
            self.accept(",")
            self.term_ext_list()

    def parameter_list(self):
        """
        <parameter_list> ::= <parameter> <parameter_prime>
        """
        logging.info('parameter_list')
        self.parameter()
        self.parameter_prime()
        pass

    def parameter(self):
        """
        <parameter> ::= <parameter_name> | <string>

        TODO:
        - param_name make sense jadi token ga? atau lebih make sense make identifier aja untuk nyamain variable name, function name dan parameter name ?
        """
        logging.info("parameter")
        if self.sym == "param_name":
            self.accept("param_name")
        elif self.sym == '"':
            self.string()
        else:
            self.term()

    def parameter_prime(self):
        """
        <parameter> ::= epsilon | , <parameter_list>
        """
        logging.info("parameter_prime")
        if self.sym == ",":
            self.accept(",")
            self.parameter_list()

    def function_call(self):
        """ 
        <function_call> ::= alias_name . funct_name ( <arg_list> ) 
            | funct_name ( <arg_list> )
        """
        logging.info("function_call")

        if self.sym == "alias_name":
            self.accept("alias_name")
            self.accept(".")
            self.accept("funct_name")
            self.accept("(")
            self.arg_list()
            self.accept(")")
        elif self.sym == "funct_name":
            self.accept("funct_name")
            self.accept("(")
            self.arg_list()
            self.accept(")")


    def arg_list(self):
        """
        <arg_list> ::= <argument> <argument_prime>
        """
        logging.info("arg_list")
        self.argument()
        self.argument_prime()

    def argument(self):
        """
        <argument> ::= <term_extended>
            | <function_call>
        """
        logging.info("argument")
        if self.sym in self.term_first:
            self.term_extended()
        elif self.sym in ['funct_name', 'alias_name']:
            self.function_call()

    def argument_prime(self):
        """
        <argument_prime> ::= epsilon | , <arg_list>
        """
        logging.info("argument prime")
        if self.sym == ",":
            self.accept(",")
            self.arg_list()

    def string(self):
        """
        <string> ::= " <string_term_list> "
        """
        logging.info("string")
        self.accept('"')
        self.string_term_list()
        self.accept('"')

    def string_term_list(self):
        """
        <string_term_list> ::= <string_term> <string_term_prime>
        """
        logging.info("string_term_list")
        self.string_term()
        self.string_term_prime()

    def string_term(self):
        """
        <string_term> ::= literal | #{ var_name }
        
        TODO :
        - Add relevant definition of string term beside literals (escape seq, etc.)
        """
        logging.info("string_term")
        if self.sym == "literal":
            self.accept("literal")
        elif self.sym == "#":
            self.accept("#")
            self.accept("{")
            self.accept("var_name")
            self.accept("}")

    def string_term_prime(self):
        """
        <string_term_prime> ::= epsilon | <string_term_list>
        """
        logging.info("string_term prime")
        if self.sym in ["literal"]: 
            self.string_term_list()


# End of MVP
