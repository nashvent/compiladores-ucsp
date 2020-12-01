line (\n)
time (\[.+\])
author (\].+\:)
message (:\s.+\n)
%%

{line} { printf("%s \\\\ \\hline ", yytext); }
{author} { printf("XXXXX"); }
{time} { printf(" %s &", yytext); }
{message} { printf(" & %s ", yytext); }

%%

int main() {
    printf("\n\\begin{tabular}{|c|p{3cm}|p{8cm}|p{2cm}|} \n");
    printf("\\\\ \\hline ");
    yylex();
    printf("\n\\end{tabular} \n");
}
