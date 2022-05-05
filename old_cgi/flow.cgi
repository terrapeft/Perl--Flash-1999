#! /usr/bin/perl

open (IN, "0flower.dat");
$filename=<IN>;
$absol="../flowers/";
$file=$absol.$filename;

print "Content-Type: text/html\n\n";
print "\<img src=\"$file\" align=\"right\"\>";

