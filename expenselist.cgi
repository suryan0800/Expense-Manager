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
my %month = qw(Jan 01 Feb 02 Mar 03 Apr 04 May 05 Jun 06 July 07 Aug 08 Sep 09 Oct 10 Nov 11 Dec 12);

sub checkdate1
{
	my $d = shift @_;
	my $d1 = shift @_;
	my $d2 = shift @_;


	if(@$d[4] > @$d1[0] )
	{
		return 'true';
	}
	elsif(@$d[4] == @$d1[0])
	{
		if(@$d[1] > @$d1[1])
		{
			return 'true';
		}
		elsif(@$d[1] == @$d1[1])
		{
			if(@$d[2] < @$d1[2])
			{
				return 'false';
			}			
			else
			{
				return 'true';
			}
		}
		else
		{
			return 'false';
		}
	}
	
	else
	{
		return 'false';
	}
}

sub checkdate2
{

	my $d = shift @_;
	my $d1 = shift @_;
	my $d2 = shift @_;
	
	if(@$d[4] < @$d2[0])
	{
		return 'true';
	}
	elsif(@$d[4] == @$d2[0])
	{
		if(@$d[1] < @$d2[1])
		{
			return 'true';
		}
		elsif(@$d[1] == @$d2[1])
		{
			if(@$d[2] > @$d2[2])
			{
				return 'false';
			}
			else
			{
				return 'true';
			}
		}
		else
		{
			return 'false';
		}
	}
	else
	{
		return 'false';
	}
}

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
p("From Date :",input({-type=>'date', -name=>'date1'})).
p("To Date",input({-type=>'date', -name=>'date2'})).
p(submit("Search"))).end_form();

if($cgi->param("date1") && $cgi->param("date2"))
{
	
	$spendings = 0;
	print 	CGI::center(p("Expense Table for the Dates : ".$cgi->param("date1")." To ".
	$cgi->param("date2")));
	my @date1 = split /-/,$cgi->param('date1');
	my @date2 = split /-/,$cgi->param('date2');
	
	print "<font size='6'><center><table border=1 width='1000' >";
	foreach $x(@list)
	{
		@date = split (/ /,@$x[0]);
		$date[1] = $month{$date[1]};
		
		my $check1 = checkdate1(\@date,\@date1,\@date2);
		my $check2 = checkdate2(\@date,\@date1,\@date2);
		if($check1 eq 'true' && $check2 eq 'true')
		{

			$spendings += @$x[1]; 
			print "<tr><td>@$x[0]</td><td>@$x[1]</td><td>@$x[2]</td></tr>";
		}	
	}
	print "</table></center></font>";
	print CGI::center(p("Total Spendings  "." $spendings"));
	
}

print end_html();























