#! /usr/bin/perl

$countfile = "c2ezcount.dat";
$digit_dir = "http://gris-souris.virtualave.net/images/digits";
$ending ="gif";

open (ALL, $countfile);
$count=<ALL>;
chomp($count);
$num = $length = length($count);
while ($num > 0) {
   $NUMS{$num} = chop($count);
   $num--;
}
$i = 1;
print "Content-type: text/html\n\n";
while ($i <= $length) {
         print"<img src=\"$digit_dir/$NUMS{$i}\.$ending\">";
   $i++;
 }
exit(0);


