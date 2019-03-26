#!/usr/bin/perl
#register.cgi

use strict;
use warnings;

use CGI(':standard');

my $table;
my $cgi = new CGI;

print header().start_html("Register Expense");
print CGI::center(h1("Register Expense"));
print br();
my $time1 = localtime();
print CGI::center(p("Date and Time : " ,$time1));
print br();
print CGI::center(start_form().
p("Amount :",input({-type=>'number',-name=>'amount',-min=>'1',-value=>'10'})).br().p("Purpose : ",textfield('purpose')).br().p(submit("Register")));

if($cgi->param('amount'))
{
	if(open($table,">> /usr/lib/cgi-bin/expensetable.txt"))
	{
		print $table "$time1".",".$cgi->param('amount').",".$cgi->param('purpose');
		print $table "\n";
		close($table);
		print CGI::center(p("Successfully Registered"));
	}
	else
	{
		print CGI::center(p("Unable to open File"));
	}
	
}
else
{
	print CGI::center(p("Press Register to Register"));
}


print end_html();






