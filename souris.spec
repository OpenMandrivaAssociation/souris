Summary:	Tool to visualize mouse clicks
Name:		souris
Version:	0.2
Release:	%mkrel 5
Source0:	%{name}-%{version}.tgz
License:	GPLv2+
Group:		Development/X11
Url:		https://www.duberga.net/souris/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk2-devel libxtst-devel

%description
souris is a tool to visualize mouse clicks,
using the X Record Extension Library.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.png
