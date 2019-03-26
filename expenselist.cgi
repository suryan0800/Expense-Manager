#!/usr/bin/perl
#expenselist.cgi

use strict;
use warnings;

use CGI(':standard');

my $cgi = new CGI;

my $table;
my @l;
my @list;
my @seperate;
my $x;
my $spendings;
my $size;
my $i;
my @date;

if(open($table,"< /usr/lib/cgi-bin/expensetable.txt"))
{
	@l= <$table>;
	
}
for($x = 0; $x < @l; $x++)
{
	@seperate = split(/,/,$l[$x]);
	chomp $seperate[2];
	for($i = 0; $i<3; $i++)
	{
		$list[$x][$i] = $seperate[$i];
	}	
}

print header().start_html("View Expense ");
print CGI::center(h1("View Expense "));
print CGI::center(start_form().
'<select name="month">
	<option value="Jan">Janauary</option>
	<option value="Feb">February</option>
	<option value="Mar">March</option>
	<option value="Apr">April</option>
	<option value="May">May</option>
	<option value="Jun">June</option>
	<option value="Jul">July</option>
	<option value="Aug">August</option>
	<option value="Sep">September</option>
	<option value="Oct">October</option>
	<option value="Nov">November</option>
	<option value="Dec">December</option>
</select>'.p(submit("Search"))).end_form();

if($cgi->param("month"))
{
	$spendings = 0;
	print 	CGI::center(p("Spendings Table for the Month : ".$cgi->param("month")));
	print "<center><table border=1>";
	foreach $x(@list)
	{
		@date = split (/ /,@$x[0]);
		if($date[1] eq $cgi->param("month"))
		{
			$spendings += @$x[1]; 
			print "<tr><td>@$x[0]</td><td>@$x[1]</td>><td>@$x[2]</td></tr>";
		}
	}
	print "</table></center>";
	print CGI::center(p("Spendings of ".$cgi->param("month")." Month : "." $spendings"));
}




print end_html();























