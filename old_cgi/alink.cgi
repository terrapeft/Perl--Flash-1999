#! /usr/bin/perl

&parse_form;
open (OUT, "> 0frlinks.dat");
print OUT "Ира\|$FORM{'T1'}\n";
print OUT "Юра\|$FORM{'T2'}\n";
print OUT "Дима\|$FORM{'T3'}\n";
print OUT "Рост\|$FORM{'T4'}\n";
close (OUT);

print "Content-Type: text/html\n\n";
print <<"sss";
<table border="0" width="100%" bgcolor="#808080">
  <tr>
    <td width="100%"><b><font size="3" face="Arial" color="#FFFF00">Операция
      выполнена успешно.</font></b></td>
  </tr>
</table>
sss
open (IN, "0frlinks.dat");
print "<p><font face=\"Arial\"><blockquote>";
while (<IN>)
{
($a, $b)=split(/\|/, $_);
print "$a&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$b<br>";
}
print "</font></p>";
print <<"ddd";
  <p>&nbsp;</p>
  <p><font face="Arial"><a href="admin.cgi">Вернуться. </a></font></p>
</blockquote>
ddd

sub parse_form{
    if ($ENV{'REQUEST_METHOD'} eq 'POST') {
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
        @pairs = split(/&/, $buffer);
        foreach $pair (@pairs) {
            ($name, $value) = split(/=/, $pair);
            $value =~ tr/+/ /;
            $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
            $value =~ s/<!--(.|\n)*-->//g;
            $value =~ s/[;><&\*`\|]//g;
            $value =~ s/^\s+//;
	    $value =~ s/\s+$//;
            $FORM{$name} = $value;
        }
    }
    else {          
print "Content-type: text/html\n\n";
print "System error....\n";
exit;
    }  
}


