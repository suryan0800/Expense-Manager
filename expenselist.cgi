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
           
			if( int(@$d[2]) < int(@$d1[2]))
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
            
			if(int(@$d[2]) > int(@$d2[2]))
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

print header();

print <<eof;
<html>
<head>
<title> View Expense</title>
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet"> 
<style>

button {
  background-color: #778899;
   border: 2px solid white;
  border-radius: 5px;
  color: white;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-weight: bold;
  width: 100px;
  height: 35px;
  font-size: 15px;
  margin: 4px 2px;
  cursor: pointer;
}

input
{
  background-color: white;
  border: 1px solid black;
  border-radius: 5px;
  color: black;
  padding: 4px 15px;
  text-decoration: none;
  display: inline-block;
  font-weight: normal;
  width: 200px;
  font-size: 20px;
  margin: 2px 2px;
  cursor: pointer;
}

h1 
{
	color : white;
	font-family: 'Roboto', sans-serif;
	padding : 10px;
	border-bottom : 1px solid white;
	width : 600px;
	margin : auto;
}

h3
{
	color : white;
	font-family: 'Roboto', sans-serif;
	padding : 10px;
	border-bottom : 1px solid white;
	font-size: 20px;
	font-weight: bolder;
	width : 600px;
	margin : auto;
}

p
{
	color : white; 
	text-align : center; 
	width : 500px; 
	font-size: 20px;
	margin : 20px auto;
}

table
{
	color : white; 
	text-align : center; 
	width : 600px; 
	font-style : bold;
	font-size: 20px;
	border : 1px solid black;
	#background-color : #aabbcc;
	margin : 20px auto;

}

</style>
</head>
<body style = "background : #002447; ">

<a href = "main.cgi"><button type = "button" >Home</button></a>	

<div class = "container" style = "width : 1000px; margin : 100px auto; text-align : center;">	


eof


print CGI::center(h1("View Expense "));
print CGI::center(start_form().
p("From Date :",input({-type=>'date', -name=>'date1'})).
p("To Date :",input({-type=>'date', -name=>'date2'})).
p(submit("Search"))).end_form();

if($cgi->param("date1") && $cgi->param("date2"))
{
	my @list4;
	$spendings = 0;
	print 	CGI::center(h3("Expense Table for the Dates : ".$cgi->param("date1")." To ".
	$cgi->param("date2")));
	my @date1 = split /-/,$cgi->param('date1');
	my @date2 = split /-/,$cgi->param('date2');
	my $f=0;
    my @dat;
	print "<font size='6'><center><table border=1 width='1000' >";
	print "<tr><td>Date</td><td>Amount</td><td>Product</td></tr>";
	foreach $x(@list)
	{
       
        @date = split (/  /,@$x[0]);      
        @dat = split (/ /,$date[1]);
        @date = split (/ /,@$x[0]);
        if ( @dat )
        {
            $date[2] = "0"."$dat[0]";
            for( my $e = 3 ; $e < @date ; $e++)
            {
            $date[$e] = $date[$e+1];
            }
        }
        if ( !@dat )
        {
         @date = split (/ /,@$x[0]);
        }
        $date[1] = $month{$date[1]};
		
		my $check1 = checkdate1(\@date,\@date1,\@date2);
		my $check2 = checkdate2(\@date,\@date1,\@date2);
		if($check1 eq 'true' && $check2 eq 'true')
		{
            $spendings += @$x[1]; 
            my $as = @$x[1];
            my $bs = @$x[2];
			print "<tr><td>@$x[0]</td><td>@$x[1]</td><td>@$x[2]</td></tr>";
			$list4[$f][0] = $as;
            $list4[$f][1] = $bs;
            $f++;
		}	
	}
	print "</table></center></font>";
	print CGI::center(p("Total Spendings  "." $spendings"));

    
     
    
     my @req ;
     for($x=0; $x < @list4 ; $x++)
     {
     
      $req[$x]= $list4[$x][1] ;
     
     }

     my %unique = ();
     foreach my $item (@req)
     {
        $unique{$item} =1;
     }
     my @myuniquearray = keys %unique;

     my @sumunique ;
     my $y = 0;

     foreach my $item (@myuniquearray)
     {
        my $sm=0;
        for($x=0; $x < @list4 ; $x++)
        {
            if ($item eq $list4[$x][1])
            {
             $sm = $sm + $list4[$x][0];
            }
        }
        $sumunique[$y]= $sm ;
        $y ++;
     }

     print br();
     print CGI::center(h3(" Itemwise Spendings "));

     print "<font size='6'><center><table border=1 width='1000' >";
     print "<tr><td>Product</td><td>Amount</td></tr>";

    

      for($x=0; $x < @myuniquearray ; $x++)
      {
        print "<tr><td>$myuniquearray[$x]</td><td>$sumunique[$x]</td></tr>";
      }

     print "</table></center></font>";
	
}

print "</div>";
print end_html();























