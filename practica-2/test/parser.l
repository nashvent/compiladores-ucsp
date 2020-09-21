digito [0-9]
entero {digito}+
real {entero}\.{entero}
%%
{entero} { printf("TOKEN: [%s] ENTERO", yytext); }
{real} { printf("TOKEN: [%s] ENTERO", yytext); }
