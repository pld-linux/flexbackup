Summary:	Flexible backup script
Summary(pl):	Elastyczny skrypt do tworzenia kopii zapasowych
Name:		flexbackup
Version:	1.2.1
Release:	2
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://flexbackup.sourceforge.net/tarball/%{name}-%{version}.tar.gz
# Source0-md5:	4955c89dbee354248f354a9bf0a480dd
URL:		http://www.flexbackup.org/
Requires:	afio
Requires:	buffer
Requires:	fileutils
Requires:	grep
Requires:	perl-base
#Requires:	bzip2 or gzip or zip - your mileage may vary
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flexible backup script.

Features:
- Easy to configure
- Uses dump, afio, tar, or cpio with the flick of a switch
- Backup, extract, compare, list modes
- Compression and buffering for all backup types
- Full (0) and 1-9 levels of incremental backup
- Keeps a table of contents so you know whats on each tape
- Does remote filesystems (over rsh/ssh; no special service)
- Works with IDE/SCSI tapes on Linux/FreeBSD, Linux ftape, or disk
  files
- Nice log files

%description -l pl
Elastyczny skrypt do tworzenia kopii zapasowych.

Zalety:
- ³atwy w konfiguracji
- umo¿liwia tworzenie kopii zapasowych programami takimi jak: dump,
  afio lub cpio
- tryby tworzenia, odtwarzania, porównywania oraz wy¶wietlania
  zawarto¶ci kopii
- kompresja oraz buforowanie dla wszystkich typów kopii
- pe³ne oraz przyrostowe tworzenie archiwów
- spis tre¶ci
- zdalne tworzenie kopii zapasowych
- wspó³pracuje ze streamerami IDE/SCSI
- dziennik tworzonych kopii zapasowych

%prep
%setup  -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_mandir}/man5
install -d $RPM_BUILD_ROOT%{_var}/{lib,log}/flexbackup

install flexbackup $RPM_BUILD_ROOT%{_bindir}
install flexbackup.conf $RPM_BUILD_ROOT%{_sysconfdir}
install flexbackup.1 $RPM_BUILD_ROOT%{_mandir}/man1
install flexbackup.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README TODO faq.html
%attr(755,root,root) %{_bindir}/flexbackup
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/flexbackup.conf
%dir %{_var}/lib/flexbackup
%dir %{_var}/log/flexbackup
%{_mandir}/man?/*
