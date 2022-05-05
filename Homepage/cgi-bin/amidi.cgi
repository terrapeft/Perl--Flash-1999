#! /usr/bin/perl

$filepath="../top.htm";

&parse_form;
open (IN, "+<$filepath") || die "Can't open your titul, Galina !!!. Call me 448 5576";
$out='';
while (<IN>) 
{
s/<bgsound src=\".*\" loop=\"0\">/<bgsound src=\"\.\.\/midi\/$FORM{'mzmid'}\" loop=\"0\">/;
$out.=$_}

seek(IN, 0, 0) || die "Seeking: $!";
print IN $out  || die "Printing: $!";
truncate(IN, tell(IN)) || die "Truncating: $!";
close(IN) || die "Closing: $!";

print "Content-Type: text/html\n\n";
print <<"sss";
<table border="0" width="100%" bgcolor="#808080">
  <tr>
    <td width="100%"><b><font size="3" face="Arial" color="#FFFF00">Операция
      выполнена успешно.</font></b></td>
  </tr>
</table>
<blockquote>
  <p><font face="Arial">Имя файла изменено на: <b> $FORM{'mzmid'}</b></font></p>
  <p><font face="Arial"><a href="admin.cgi">Вернуться.
  </a></font></p>
</blockquote>
sss

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
