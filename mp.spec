%define		basever	5

Name:		mp
Version:	5.2.1
Release:	1
Summary:	Minimum Profit - Programmer Text Editor	
Group:		Editors 
License:	GPL
URL:		http://triptico.com
Source0:	http://triptico.com/download/%{name}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	ncurses-devel
BuildRequires:	qt4-devel
Provides:	minimum-profit = %{version}-%{release}
Patch0:		mp-5.2.1-prll.patch


%description

Minimum Profit (mp) is a text editor for programmers. Among its features
are the following:

 - Fully scriptable using a C-like scripting language.
 - Unlimited undo levels.
 - Complete Unicode support.
 - Multiple files can be edited at the same time and blocks copied
   and pasted among them.
 - Syntax highlighting for many popular languages / file formats: C, C++,
   Perl, Shell Scripts, Ruby, Php, Python, HTML...
 - Creative use of tags: tags created by the external utility _ctags_
   are used to move instantaneously to functions or variables inside
   your current source tree. Tags are visually highlighted (underlined),
   and symbol completion can be triggered to avoid typing your own function
   names over and over.


%prep
%setup -q
%patch0 -p1

%build
sh config.sh --prefix="/usr" --without-win32 --with-kde4 
%make

%install
mkdir -p %{buildroot}/%{_bindir}
%makeinstall_std

%files
%doc COPYING README
%{_bindir}/%{name}-%{basever}
%{_bindir}/mpsl
%{_mandir}/man1/%{name}-%{basever}.*
%{_docdir}/%{name}-%{basever}
%{_datadir}/%{name}-%{basever}
%{_datadir}/locale/
