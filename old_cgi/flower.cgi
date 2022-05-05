#! /usr/bin/perl

open (IN, "0flower.dat");
$file=substr(<IN>, 4, 3);
$file++;
$filename="flow".$file.".gif";
$absol="../flowers/";
$file=$absol.$filename;
close(IN);
	
if (-e $file)
{
    open (OUT, "> 0flower.dat");
    print OUT "$filename\n";
    print "Content-Type: text/html\n\n";
    print "\<img src=\"$file\" align=\"right\"\>";
} 
else {
    $file="000";
    $write="flow".$file.".gif";
    open (OUT, "> 0flower.dat");
    print OUT "$write\n";
    $write=$absol.$write;
    print "Content-Type: text/html\n\n";
    print "\<img src=\"$write\" align=\"right\"\>";
}

