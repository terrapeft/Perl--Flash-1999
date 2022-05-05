#!/usr/bin/perl

&parse_form;
$reply=wintokoi($FORM{'reply'});
$subj=wintokoi($FORM{'subj'});
$messa=wintokoi($FORM{'messa'});

$mailprog = '/usr/sbin/sendmail';
$snmail="witaly\@mail.spbnit.ru";
open (MAIL, "|$mailprog -t");
print MAIL "To: $snmail\n";
print MAIL "From: $reply < $reply >\n";
print MAIL "Subject: $subj \n\n";
print MAIL "$messa \n\n";
print MAIL "$reply";
close(MAIL);

&endi;


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

sub wintokoi {
    my $pvdcoderwin=shift;
    $pvdcoderwin=~ tr/\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF/\xE1\xE2\xF7\xE7\xE4\xE5\xF6\xFA\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF2\xF3\xF4\xF5\xE6\xE8\xE3\xFE\xFB\xFD\xFF\xF9\xF8\xFC\xE0\xF1\xC1\xC2\xD7\xC7\xC4\xC5\xD6\xDA\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD2\xD3\xD4\xD5\xC6\xC8\xC3\xDE\xDB\xDD\xDF\xD9\xD8\xDC\xC0\xD1/;
return $pvdcoderwin;
}


sub endi {
print "Content-type: text/html\n\n";
print <<"ALL"

<html>

<head>
<meta http-equiv="Content-Language" content="ru">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<META HTTP-EQUIV = "REFRESH" CONTENT = "5; URL=http://right-now.homepage.dk/">
<title>Thanks</title>
</head>

<body bgcolor="#FFFFFF" topmargin="0" leftmargin="0">

<body bgcolor="#FFFFFF">
<table border="0" width="100%" bgcolor="#800000" cellspacing="0" cellpadding="0">
  <tr>
    <td width="100%"><b><font face="Arial" size="3" color="#FFCC00">Yahooo !</font></b></td>
  </tr>
</table>
<blockquote>
  <p><b><font face="Arial" size="3" color="#800000">Все в порядке !<br>
  Через пять сек попадете обратно.</font></b></p>
</blockquote>

<blockquote>
  <p><b><font face="Arial" size="3" color="#800000">Thanks. This letter was sent
  successfully.<br>
  You'll be redirected back in 5 seconds.</font></b></p>
</blockquote>

</body>

</html>

ALL

}