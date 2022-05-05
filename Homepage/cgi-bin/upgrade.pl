#! /usr/bin/perl

print "Content-type: text/html\n\n";
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
if ($buffer eq "") {
 $buffer=$ENV{'QUERY_STRING'};
}
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
   ($name, $value) = split(/=/, $pair);
    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    $in{$name} = $value;
}

require "pvdgb.cfg";

if (!$buffer) {
print qq~
<html>
<head>
<title>Обновление базы гостевой книги</title>
</head>
<body leftmargin=0 topmargin=0 marginheight="0" marginwidth="0">
<form method=post action=upgrade.pl>
Для того чтоб обновить базу записей вашей старой гостевой<br>
книги под новую нажмите эту кнопку - <input type=submit value="up" name="up">
</form>
</body></html>
~;
} elsif ($in{'up'} eq "up") {
open TEMP, "<$gb_db"; @LIST=<TEMP>; $sizelist=@LIST; close TEMP;
open TEMP, ">$gb_db"; flock (TEMP,2);
for ($i=0;$i<=$sizelist;$i++) {
    $LIST[$i]=~ s/\xA4/\x01/g;
    print TEMP $LIST[$i];
}
close TEMP;
print qq~
<html>
<head>
<title>Обновление базы гостевой книги</title>
</head>
<body leftmargin=0 topmargin=0 marginheight="0" marginwidth="0">
Если вы видите только эту запись (русскую) значит все - ОК !
</body></html>
~;
}
