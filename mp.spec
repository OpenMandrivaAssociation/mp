%define		basever	5

Name:		mp
Version:	5.62
Release:	1
Summary:	Minimum Profit - Programmer Text Editor	
Group:		Editors 
License:	GPL
URL:		https://triptico.com
Source0:	https://github.com/ttcdt/mp-5.x/archive/refs/tags/%{version}.tar.gz
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Widgets)
Provides:	minimum-profit = %{EVRD}

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
%autosetup -p1 -n mp-5.x-%{version}

%build
export CXX=g++
export CPP=g++
export CC=gcc
export CFLAGS="%{optflags} -fpermissive"
./config.sh --prefix="%{_prefix}" \
            --without-win32 \
            --with-qt5 \
	    --without-qt4 \
            --without-gtk \
            --with-curses

make MOC=%{_qt5_bindir}/moc

%install
mkdir -p %{buildroot}/%{_bindir}
%make_install

%files
%doc LICENSE README
%{_bindir}/%{name}-%{basever}
#{_mandir}/man1/%{name}-%{basever}.*
%{_docdir}/%{name}-%{basever}
#{_datadir}/%{name}-%{basever}
#{_datadir}/locale/
