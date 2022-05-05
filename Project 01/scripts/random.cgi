opendir(DIR,"../images/faces") || &showErr('Access error!'); 
@files = sort(readdir(DIR));
closedir(DIR);
for($s1 = @files; $s1 >= 0; $s1--) {
	if ($files[$s1] !~ /^\d+(.gif|.jpg)/i) {
		push(@random,$files[$s1]) if $files[$s1] =~ /(.gif|.jpg)/i;
		splice(@files,$s1,1);}}


for ($i=@random; --$i;)
 { my $j = rand($i+1);
   next if $i==$j;
   $random[$i,$j]=$random[$j,$i];
 }


print "Content: text/html \n\n";

foreach $el (@random)
{
print <<"laja"
<img border="0" src="$el" width="88" height="137">

laja

 }
