Summary:	Flexible backup script
Summary(pl):	Elastyczny skrypt do tworzenia kopii zapasowych
Name:		flexbackup
Version:	0.9.8
Release:	2
License:	GPL
Group:		Applications/Archiving
Source0:	http://members.home.com/flexbackup/tarball/%{name}-%{version}.tar.gz
# Source0-md5:	5e5042794c778358dbda88c02fcdc4f0
Patch0:		%{name}-ksh.patch
URL:		http://members.home.com/flexbackup/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	afio
Requires:	buffer
Requires:	grep
Requires:	fileutils
#Requires:	bzip2 or gzip or zip - your mileage may vary

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
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}

install flexbackup $RPM_BUILD_ROOT%{_bindir}
install flexbackup.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc flexbackup.lsm CHANGES CREDITS README TODO
%attr(755,root,root) %{_bindir}/flexbackup
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/flexbackup.conf
