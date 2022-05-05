#! /usr/bin/perl
BEGIN {

	$SAVE_DIRECTORY = "/home/kotenka1359/public_html/midi/";
	$MAXIMUM_UPLOAD = 1000000;
	$ALLOW_INDEX = 0;
	$SUCCESS_LOCATION = "http://gris-souris.virtualave.net/cgi-bin/admin.cgi";
}

	$| = 1;
	chop $SAVE_DIRECTORY if ($SAVE_DIRECTORY =~ /\/$/);
	use CGI qw(:standard);
	$query = new CGI;

	if ( (!(-e $SAVE_DIRECTORY)) ||
		 (!(-W $SAVE_DIRECTORY)) ||
		 (!(-d $SAVE_DIRECTORY)) ) {
		print header;
		print <<__END_OF_HTML_CODE__;
		
		<HTML>
		<HEAD>
			<TITLE>Error: Bad Directory</TITLE>
		</HEAD>
		<BODY BGCOLOR="#FFFFFF">
		<H1>Bad Directory</H1>
		<P>
		The directory you specified:
		<BR>
		<BLOCKQUOTE>
			<TT>\$SAVE_DIRECTORY = "<B>$SAVE_DIRECTORY</B>";</TT>
		</BLOCKQUOTE>
		<BR>
		is invalid.  This problem is caused by one of the three following reasons:
		<OL>
			<LI>The directory doesn't exist.  Make sure that this directory is a complete path name, not
			    a URL or something similar.  It should look similar to <TT>/home/username/public_html/uploads</TT>
			<P>
			<LI>The directory isn't writable.  Make sure that this directory is writable by all users.  At
				your UNIX command prompt, type <TT>chmod 777 $SAVE_DIRECTORY</TT>
			<P>
			<LI>The directory you specified isn't really a directory.  Make sure that this is indeed a directory
				and not a file.
		</OL>
		
		</BODY>
		</HTML>
		
__END_OF_HTML_CODE__
		exit;
	}
	
	foreach $key (sort {$a <=> $b} $query->param()) {
		next if ($key =~ /^\s*$/);
		next if ($query->param($key) =~ /^\s*$/);
		next if ($key !~ /^file-to-upload-(\d+)$/);
		$Number = $1;
		
		if ($query->param($key) =~ /([^\/\\]+)$/) {
			$Filename = $1;
			$Filename =~ s/^\.+//;
			$File_Handle = $query->param($key);
			
			if (!$ALLOW_INDEX && $Filename =~ /^index/i) {
				print header;
				print <<__END_OF_HTML_CODE__;
				
				<HTML>
				<HEAD>
					<TITLE>Error: Filename Problem</TITLE>
				</HEAD>
				<BODY BGCOLOR="#FFFFFF">
				<H1>Filename Problem</H1>
				<P>
				You attempted to upload a file that isn't properly formatted.  The system administrator
				has decided that you can't upload files that begin with the word '<B>index</B>'. Please
				rename the file on your computer, and try uploading it again.
				<P>
				
				</BODY>
				</HTML>
	
__END_OF_HTML_CODE__
				exit;
			}
		} else {
			$FILENAME_IN_QUESTION = $query->param($key);
			
			print header;
			print <<__END_OF_HTML_CODE__;
			
			<HTML>
			<HEAD>
				<TITLE>Error: Filename Problem</TITLE>
			</HEAD>
			<BODY BGCOLOR="#FFFFFF">
			<H1>Filename Problem</H1>
			<P>
			You attempted to upload a file that isn't properly formatted.  The file in question 
			is <TT><B>$FILENAME_IN_QUESTION</B></TT>  Please rename the file on your computer, and
			attempt to upload it again.  Files may not have forward or backward slashes in their 
			names.  Also, they may not be prefixed with one (or more) periods.
			<P>
			
			</BODY>
			</HTML>

__END_OF_HTML_CODE__
			exit;
		}
		
        if (!open(OUTFILE, ">$SAVE_DIRECTORY\/$Filename")) {
            print "Content-type: text/plain\n\n";
            print "-------------------------\n";
            print "Error:\n";
            print "-------------------------\n";
            print "File: $SAVE_DIRECTORY\/$Filename\n";
            print "-------------------------\n";
	        print "There was an error opening the Output File\n";
    	    print "for Writing.\n\n";
        	print "Make sure that the directory:\n";
	        print "$SAVE_DIRECTORY\n";
    	    print "has been chmodded with the permissions '777'.\n\n";
        	print "Also, make sure that if your attempting\n";
	        print "to overwrite an existing file, that the\n";
    	    print "existing file is chmodded '666' or better.\n\n";
	        print "The Error message below should help you diagnose\n";
    	    print "the problem.\n\n";
        	print "Error: $!\n";
            exit;
        }

		undef $BytesRead;
		undef $Buffer;
		
        while ($Bytes = read($File_Handle,$Buffer,1024)) {
			$BytesRead += $Bytes;
            print OUTFILE $Buffer;
        }
		
		push(@Files_Written, "$SAVE_DIRECTORY\/$Filename");
		$TOTAL_BYTES += $BytesRead;
		$Confirmation{$File_Handle} = $BytesRead;

        close($File_Handle);
		close(OUTFILE);

        chmod (0666, "$SAVE_DIRECTORY\/$Filename");
    }

	$FILES_UPLOADED = scalar(keys(%Confirmation));

	
	if ($TOTAL_BYTES > $MAXIMUM_UPLOAD && $MAXIMUM_UPLOAD > 0) {
		foreach $File (@Files_Written) {
			unlink $File;
		}
		
		print header;
		print <<__END_OF_HTML_CODE__;
		
		<HTML>
		<HEAD>
			<TITLE>Error: Limit Reached</TITLE>
		</HEAD>
		<BODY BGCOLOR="#FFFFFF">
		<H1>Limit Reached</H1>
		<P>
		You have reached your upload limit.  You attempted to upload <B>$FILES_UPLOADED</B> files, totalling 
		<B>$TOTAL_BYTES</B>.  This exceeds the maximum limit of <B>$MAXIMUM_UPLOAD</B> bytes, set by the system 
		administrator.  <B>None</B> of your files were successfully saved.  Please try again.
		<P>
		
		</BODY>
		</HTML>
				
__END_OF_HTML_CODE__
		exit;
	}
	
	if ($SUCCESS_LOCATION !~ /^\s*$/) {
		print $query->redirect($SUCCESS_LOCATION);
	} else {
	

		print header;
		print <<__END_OF_HTML_CODE__;
		
		<HTML>
		<HEAD>
			<TITLE>Upload Finished</TITLE>
		</HEAD>
		<BODY BGCOLOR="#FFFFFF">
		<H1>Upload Finished</H1>
		<P>
		You uploaded <B>$FILES_UPLOADED</B> files totalling <B>$TOTAL_BYTES</B> total bytes.  Individual
		file information is listed below:
		<PRE>
	
__END_OF_HTML_CODE__

		foreach $key (keys (%Confirmation)) {
			print "$key - $Confirmation{$key} bytes\n";
		}
		
		print <<__END_OF_HTML_CODE__;
		
		</PRE>
		<P>
		Thank you for using the File Upload! system.
		<P>
		
		</BODY>
		</HTML>

__END_OF_HTML_CODE__
		exit;	
	}
	
# 
