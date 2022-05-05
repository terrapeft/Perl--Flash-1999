#!perl
use LWP::UserAgent ();
use LWP::MediaTypes qw(guess_media_type media_suffix);
use URI ();
use HTTP::Date ();

&parse_form;
my $ua = new LWP::UserAgent;

$ua->agent("Ex-Spider v24-1");
# $ua->proxy(['http', 'ftp'], 'http://numbers.tvcc.cc.or.us:80/');
$ua->env_proxy;
print "Content-type: text/html\n\n";
print "<h2>Search engine result analizer.</h2><br>";
print "<h3>Performing search...</h3><br>";
my $rurl;
$rurl=$FORM{'engi'};
$rurl=~s/REPLACE/$FORM{'keywrds'}/;
print $rurl;


my $url = new URI::URL($rurl);
my @rawdata = ('pg','q','sc','on','hl','on','q','hotels in paris','kl','XX','stype','stext');
my $datalength = @rawdata;
my $special_characters = '\x00-\x20"#%;<>?{}|\\\\^~`\[\]\x7F-\xFF;,/?:@=&';
my $content = undef;
my $convertloop;
my $result;
for ($convertloop = 0; $convertloop < $datalength; $convertloop = $convertloop+2) {
$content .= $rawdata[$convertloop] . "=" . $rawdata[$convertloop+1] . "&";
}
chop $content;  # Removes the last & character

my $headers = new HTTP::Headers
    'Content-Type'    =>      'application/x-www-form-urlencoded',
    'MIME-Version'    =>      '1.0',
    'Date'            =>      HTTP::Date::time2str(time),
    'Content-length'  =>      length($content),
    'Accept'          =>      'text/html',
    ;

my $request = new HTTP::Request GET => $url;
my $response = $ua->request($request);
my $server_response = $response->as_string;
mkdir($FORM{'engi'}, 0777);
open(FILE, ">$FORM{'engi'}\/$FORM{'keywrds'}\_result\.htm");
print FILE "$server_response\n";
close(FILE);

APAGES:

open(FILE2,"$FORM{'engi'}\/$FORM{'keywrds'}\_result\.htm");
@server_response = <FILE2>;
close(FILE2);

#AV
if ($rurl=~m/altavista/)
{
 $n=1; $nxtl=0;
 foreach $fileline (@server_response) {
  $fileline =~ s/\n//g;
  if ($nxtl==1) {
   (@mass) = split(/\">/,$fileline);
   (@lnk) = split(/=\"/,$mass[0]);
   push (@links,$lnk[1]);
   $nxtl=0;
  }
  if ($fileline =~ /<b>$n\. <\/b>/) {
   $nxtl=1;
   $n++;
  }
 }
}

# AZ
if ($rurl=~m/anzwer/){
foreach $fileline (@server_response) {
 $fileline =~ s/\n//g;
 if ($fileline =~ /class=result/) {
  (@mass) = split(/\' class=result/,$fileline);
  $empty=pop (@mass);
  foreach $el (@mass) {
   @link=split (/<a href=\'/,$el);
   @llink=split (/\' target/,$link[1]);
   push (@links,$llink[0]);
  }
 }
}
}

$n=1;
foreach $link (@links) {
$request = new HTTP::Request GET => $link;
$response = $ua->request($request);
$server_response = $response->as_string;
print "Saving: $FORM{'engi'}\/$FORM{'keywrds'}\_$n\.htm\n";
open(FILE, ">$FORM{'engi'}\/$FORM{'keywrds'}\_$n\.htm");
print FILE "$server_response\n";
close(FILE);
$n++;
}

ARESULTS:

# define keywords
$keyws=$FORM{'keywrds'};
$keyws=~tr/+/ /; # no '+' sign
push (@skeyw,$keyws);
$keyws=~tr/a-z/A-Z/; # all upper case
push (@skeys,$keyws);
$keyws=~tr/A-Z/a-z/; # all lower case
push (@skeys,$keyws);
@words=split(/ /,$keyws);
$s=1;
foreach $word(@words) {
$keyws="";
$w=0;
foreach $word(@words) {
if ($w<$s) { $word=ucfirst($word); }
$keyws="$keyws $word";
$w++;
}
$keyws=substr($keyws,1,length($keyws));
push (@skeys,$keyws);
$s++;
}
foreach $word(@words) {
push (@skeys,$word);
$word=lcfirst($word);
push (@skeys,$word);
}

open(FILER,">$FORM{'engi'}\/$FORM{'keywrds'}\_stats\.htm");
print FILER "Analizing results....\n";
print FILER "for keyword string: $keyws\n";
for ($i=1; $i<11; $i++) {
$resfile="$FORM{'engi'}\/$FORM{'keywrds'}\_$i\.htm";
print FILER "File: $resfile\n";
open(FILE,"$resfile");
@filedata = <FILE>;
close(FILE);

undef (@keywc);
undef (@keywn);
$textlen=0;
$filelen=0;
$flenf=0;
foreach $fileline (@filedata) {
 if ($fileline =~ /\</) { $flenf=1; }
 if ($flenf==1) {
  $filelen+=length($fileline)+1;
  $fileline =~ s/\n//g;
  $n=0;
  foreach $keyws (@skeys) {
   if ($fileline =~ /$keyws/) { $keywc[$n]++; }
   $n++;
  } # keyword strings
$fileline=~s/<.*?>//gs;
$textlen+=length($fileline);
  $n=0;
  foreach $keyws (@skeys) {
   if ($fileline =~ /$keyws/) { $keywn[$n]++; }
   $n++;
  } # keyword strings


 } # html starts
} # filelines
if ($textlen) {
$perc = 100 / ($filelen / $textlen);
$percs="$perc";
$percs=substr($perc,0,4);
}
else { $percs=0; }
print FILER "  File length: $filelen\n";
print FILER "  Text length: $textlen  $percs%\n";

  $n=0;
  foreach $keyws (@skeys) {
if ($keywc[$n]) { print FILER "  Keyword count total  : $keyws  $keywc[$n]\n"; }
if ($keywn[$n]) { print FILER "  Keyword count no tags: $keyws  $keywn[$n]\n"; }
   $n++;
  } # keyword strings

} #files $i
close (FILER);
&linker;
exit;


sub parse_form{
    if ($ENV{'REQUEST_METHOD'} eq 'POST') {
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
        @pairs = split(/&/, $buffer);
        foreach $pair (@pairs) {
            ($name, $value) = split(/=/, $pair);
            $value =~ tr/+/ /;
            $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
            $value =~ s/<!--(.|\n)*-->//g;
            $value =~ s/[;><\*`\|]//g;
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

sub linker {
opendir(DIR,$FORM{'engi'}) || die ('Error Accessing Directory'); 
@files = sort(readdir(DIR));
closedir(DIR);
for($s1 = @files; $s1 >= 0; $s1--) {
	if ($files[$s1] !~ /^\d+(.mid|.wav)/i) {
		push(@files2,$files[$s1]) if $files[$s1] =~ /(.mid|.wav)/i;
		splice(@files,$s1,1);
	}
}
@files2 = sort(@files2);
print @files2;
}
