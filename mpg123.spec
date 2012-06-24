Summary:     MPEG audio player
Summary(pl): Odtwarzacz plik�w audio MPEG
Name:        mpg123
Version:     0.59o
Release:     5
Group:       Applications/Sound
Group(pl):   Aplikacje/D�wi�k
Copyright:   Freely distributable for non-commercial use
Source:      http://www-ti.informatik.uni-tuebingen.de/~hippm/mpg123/%{name}-%{version}.tar.gz
Patch0:      mpg123-opts.patch
Patch1:      mpg123-sparc.patch
URL:         http://www-ti.informatik.uni-tuebingen.de/~hippm/mpg123.html
Buildroot:   /tmp/%{name}-%{version}-root

%description
Mpg123 is a fast, free(for non-commercial use) and portable MPEG audio
player for Unix.  It supports MPEG 1.0/2.0 layers 1, 2 and 3 (those famous
"mp3" files).  For full CD quality playback (44 kHz, 16 bit, stereo) a
Pentium, SPARCstation10, DEC Alpha or similar CPU is required. Mono and/or
reduced quality playback (22 kHz or 11 kHz) is even possible on 486 CPUs.

%description -l pl
Mpg123 jest szybkim, darmowym (przy u�ytku niekomercyjnym) oraz uniwersalnym
dekoderem plik�w d�wi�kowych MPEG dla system�w Unixowych.  Obs�uguje
standart MPEG 1.0/2.0 warstwy 1, 2 oraz 3 (s�ynne "mp3").  Do uzyskania
pe�nej jako�ci CD wymagany jest silny procesor (Pentium, SPARCstation10, DEC
Alpha lub podobny). Ni�sz� jako�� (22 lub 11 kHz) mo�na uzyska� ju� na
procesorach 486.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%ifarch i386
make linux
%else
make linux-%{buildarch}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}
install mpg123 $RPM_BUILD_ROOT/usr/bin
install mpg123.1 $RPM_BUILD_ROOT/usr/man/man1

gzip -9nf BUGS COPYING CHANGES JUKEBOX README \
	$RPM_BUILD_ROOT/usr/man/man1/mpg123.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,COPYING,CHANGES,JUKEBOX,README}.gz 
%attr(755,root,root) /usr/bin/mpg123
/usr/man/man1/mpg123.1.gz

%changelog
* Fri Nov 27 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.59o-5]
- updated URL and Source,
- added support for more architectures (modified mpg123-opts.patch
  and added mpg123-sparc.patch).

* Mon Sep 14 1998 Marek Obuchowicz <elephant@shadow.eu.org>
  [0.59o-4]
- added pl translation.

* Mon Feb 16 1998 Karsten Weiss <karsten@addx.au.s.shuttle.de>
- Upgraded to 0.59o

* Sun Feb 15 1998 Karsten Weiss <karsten@addx.au.s.shuttle.de>
- Upgraded to 0.59n
- Fixed absolute paths in spec file

* Tue Dec 02 1997 Trond Eivind Glomsr�d <teg@pvv.ntnu.no>
- Corrected the copyright
- The binary is now compiled for pentium (with egcs-971201)
- Compiled with Red Hat 5.0
- a little patch to make it respect RPM_OPT_FLAGS

* Thu Nov 20 1997 Greg Boehnlein <damin@nacs.net>
- Rebuilt for RedHat Mustang using Glibc
