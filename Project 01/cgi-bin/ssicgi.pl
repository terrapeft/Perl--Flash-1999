# ssi test script
$| =  1;
print "Content-type: text/html\n\n";


for ($i=0; $i <5; $i++) {
    $date = localtime();
    print "This is ssicgi $i on $date<br>\n";
    sleep(1);
}
