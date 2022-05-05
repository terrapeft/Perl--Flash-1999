#! /usr/bin/perl

%decode=(
	"kir.gif" => "sir Kirill",
        "redhood.gif" => "Red Hood",
        "taagman.gif" => "Darth Taag Men",
        "tucker.gif" => "Tucker"
        );

&getfiles;
@all=@done;
shuffle(\@all);
&printer;


sub printer {
print "Context-type: text/html\n\n";
print <<"a1";
<table border="0"><tr>
a1
foreach $i (@all){
print <<"a2";
<td width="25%" align="center"><img border="0" src="../images/faces/$i"></td>
a2
 }
print <<"a3";
</tr><tr>
a3

foreach $i (@all){
print <<"a4";
<td width="25%" align="center"><b><font face="Arial" size="2">$decode{"$i"}</font></b></td>
a4
 }
print <<"a5";
</tr></table>
a5

}#sub

sub getfiles {
opendir(DIR,"../images/faces") || die('Error Accessing Pics Directory'); 
@files = sort(readdir(DIR));
closedir(DIR);
for($s1 = @files; $s1 >= 0; $s1--) {
	if ($files[$s1] !~ /^\d+(.jpg|.gif)/i) {
		push(@done,$files[$s1]) if $files[$s1] =~ /(.jpg|.gif)/i;
		splice(@files,$s1,1);
	}
}
@done = sort(@done);
}


sub shuffle {
my $array=shift;
my $i;

for ($i=@$array; --$i;){
	my $j=int rand ($i+1);
	next if $i==$j;
	@$array[$i,$j]=@$array[$j,$i];
	}

}