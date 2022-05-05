#! /usr/bin/perl
use CGI qw(param);

open(OB, "0obnovka.dat");
$i=0;
while (<OB>){
 $_=~s/#.*//;
 @upgr[$i]=$_;
 $i++
}
$out=param("ln");
print "Content-Type: text/html\n\n";
print $upgr[$out];