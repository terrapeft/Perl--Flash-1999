#! /usr/bin/perl
require 'cgi-lib.pl';
$TMP = '/tmp/';
$UPLOADDIR = '/home/kotenka1359/public_html/midi/';
$CONTENT_TYPE = $ENV{'CONTENT_TYPE'};
$CONTENT_LENGTH = $ENV{'CONTENT_LENGTH'};
$BUF_SIZ = 16834;
# make tempfile name
do {
    $tempfile = $TMP."formupload-".time 
} until (!(-e $tempfile));
if ($CONTENT_TYPE =~ /^multipart\/form-data/) {
    # save form data to a temporary file
    ($boundary = $CONTENT_TYPE) =~ s/^multipart\/form-data\; boundary=//;
    open(TMPFILE,">$tempfile"); 
    $bytesread = 0;
    while ($bytesread < $CONTENT_LENGTH) {
     $len = sysread(STDIN,$buffer,16834); 
     syswrite(TMPFILE,$buffer,$len); 
     $bytesread += $len;
    }
    close(TMPFILE);
    # parse temporary file
    undef %input;
    open(TMPFILE,$tempfile);
    $line = <TMPFILE>; # should be boundary; ignore
    while ($line = <TMPFILE>) {
     undef $filename;
     $line =~ s/[Cc]ontent-[Dd]isposition: form-data; //;
     ($name = $line) =~ s/^name=\"([^\"]*)\".*$/$1/; 
     if ($line =~ /\; filename=\"[^\"]*\"/) {
         $line =~ s/^.*\; filename=\"([^\"]*)\".*$/$1/;
         $filename = "$UPLOADDIR$line";
     }
     $line = <TMPFILE>; # blank line
     if (defined $filename) {
         open(NEWFILE,">$filename"); 
     }
     elsif (defined $input{$name}) { 
         $input{$name} .= "\0";
     }
     while (!(($line = <TMPFILE>) =~ /^--$boundary/)) {
         if (defined $filename) {
          print NEWFILE $line;
         }
         else {
          $input{$name} .= $line;
         }
     }
     if (defined $filename) {
         close(NEWFILE); 
     }
     else {
         $input{$name} =~ s/[\r\n]*$//;
     }
    }
    close(TMPFILE);
    unlink($tempfile);
    # print success message
    print &PrintHeader,&HtmlTop("Success!"),&PrintVariables(%input),&HtmlBot; 
}
else {
    print &PrintHeader,&HtmlTop("Wrong Content-Type!"),&HtmlBot;
} 
