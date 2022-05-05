open (IN, "+<$ARGV[0]");
$out='';
while (<IN>)
{
s/\t//g;
if (m/<body/i) {$telo=1};
s/\n//g if $telo==1;

$out.=$_;
}
seek(IN, 0, 0) || die "Seeking: $!";
print IN $out  || die "Printing: $!";
truncate(IN, tell(IN)) || die "Truncating: $!";
close(IN) || die "Closing: $!";
