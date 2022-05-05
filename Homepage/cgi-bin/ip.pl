#! /usr/bin/perl
$host = $ENV{'REMOTE_HOST'}; 
print "Content-Type: text/html\n\n";
print "Your IP $host";
