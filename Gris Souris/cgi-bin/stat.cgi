#! /usr/bin/perl
#For Gris Souris
open (STAT, "c2ezcount.dat");
$hits=<STAT>;
print "Content-type: text/html\n\n";
print "—четчик нащелкал: $hits";
exit(0);