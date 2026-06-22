grammar Compilador;

prog: stmt+ (NEWLINE)*;

stmt: 
    if_stmt
    | while_stmt
    | do_while_stmt
    | variable_declaration
    | comparison_expr
    | stmt_2

    | expr_arithmetic
    | TYPE_STRING
    | '(' stmt (',' stmt)* ')'
    | BOOL
    | WS
    ;

if_stmt: IF '(' expr ')' block (ELSE block)? 
            | IF '(' expr ')' ':';
while_stmt: WHILE '(' expr ')' block;
do_while_stmt: DO block WHILE '(' expr ')';

stmt_2: 
    DIGITAL_READ '(' stmt ')'
    | DIGITAL_WRITE '(' stmt ',' stmt ')'
    | ANALOG_READ '(' stmt ')'
    | ANALOG_WRITE '(' stmt ',' stmt ')'
    | PIN_TYPE '(' stmt ')'
    | PIN_MODE '(' stmt ',' PIN_TYPE_ ')'
    | DELAY '(' stmt ')'
    ;

expr_arithmetic:  
        expr_arithmetic (PLUS|MINUS|ASTERISK|SLASH) expr_arithmetic
    |   TYPE_INT
    |   TYPE_REAL
    |   '(' expr_arithmetic ')'
    ;



comparison_expr: ID comparison_operator expr;

comparison_operator: EQUAL | NOTEQUAL | LESSTHENOP | BIGGERTHENOP;

expr: comparison_expr | id_expr;

variable_declaration: type (ID | TYPE_CHAR) ATT (TYPE_STRING | TYPE_INT | TYPE_REAL);

type: INT | FLOAT16 | BOOL | VOID | STRING;


id_expr: ID | TYPE_INT | TYPE_REAL | BOOL | TYPE_STRING;

block: LBRACE_P stmt* RBRACE_P;

INT: 'int';
FLOAT16: 'float';
VOID: 'void';
STRING : 'string';
BOOL: TRUE | FALSE;
TRUE: 'TRUE';
FALSE: 'FALSE';
WS: [ \t\r\n]+ -> skip;
TYPE_INT: [0-9]+;
TYPE_REAL: TYPE_INT+('.' TYPE_INT+)?;
TYPE_CHAR: [a-zA-Z];
TYPE_STRING: ('"' (TYPE_CHAR | '_' | [0-9])+ '"');
DIGITAL_READ: 'DIGITAL_READ';
DIGITAL_WRITE: 'DIGITAL_WRITE';
ANALOG_READ: 'ANALOG_READ';
ANALOG_WRITE: 'ANALOG_WRITE';
PIN_MODE: 'PIN_MODE';
PIN_TYPE: 'PIN_TYPE';
PIN_TYPE_: 'INPUT' | 'OUTPUT';
IF: 'IF';
ELSE: 'ELSE';
DO: 'DO';
WHILE: 'WHILE';
EQEQ: 'EQEQ';
DELAY: 'DELAY';
BREAK: 'BREAK';
ASTERISK: '*';
SLASH: '/';
PLUS: '+';
MINUS: '-';
ATT: '=';
EQUAL: '==';
NOTEQUAL: '!=';
LESSTHENOP: '<=';
LESS: '<';
BIGGER: '>';
BIGGERTHENOP: '>=';
QUOTATION_MARKS: '"';
LBRACE: '(';
RBRACE: ')';
LBRACE_P: '{';
RBRACE_P: '}';
COMMA: ',';
NEWLINE: [\r\n]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
