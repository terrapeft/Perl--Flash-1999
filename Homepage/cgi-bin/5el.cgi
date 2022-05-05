#! /usr/bin/perl

open (IN, "el.dat");
$file=substr(<IN>, 4, 3);
$file++;
$filename="el".$file.".gif";
$absol="../els/";
$file=$absol.$filename;
close(IN);
	
if (-e $file)
{
    open (OUT, "> el.dat");
    print OUT "$filename\n";
    print "Content-Type: text/html\n\n";
    print "\<img src=\"$file\" align=\"center\"\>";
} 
else {
    $file="000";
    $write="el".$file.".gif";
    open (OUT, "> el.dat");
    print OUT "$write\n";
    $write=$absol.$write;
    print "Content-Type: text/html\n\n";
    print "\<img src=\"$write\" align=\"center\"\>";
}

