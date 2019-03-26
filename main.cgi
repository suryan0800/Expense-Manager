#!/usr/bin/perl
#main.cgi

use strict;
use warnings; 

use CGI(':standard');

print header().start_html("Home Page ");
print CGI::center(h1("Welcome to Expense Manager"));
print br();
print CGI::center(start_form(-action=>"register.cgi").(p(submit("Register"))).end_form());
print br();
print br();
print CGI::center(start_form(-action=>"expenselist.cgi").(p(submit("View Expense"))).end_form());
print end_html();



