Summary:	MPEG audio player
Summary(pl):	Odtwarzacz plik�w audio MPEG
Name:		mpg123
Version:	0.59q
Release:	1
Group:		Applications/Sound
Group(pl):	Aplikacje/D�wi�k
Copyright:	Freely distributable for non-commercial use
Source:		http://www-ti.informatik.uni-tuebingen.de/~hippm/mpg123/%{name}-%{version}.tar.gz
Patch0:		mpg123-makefile.patch
Patch1:		mpg123-8bit.patch
URL:		http://www-ti.informatik.uni-tuebingen.de/~hippm/mpg123.html
Buildroot:	/tmp/%{name}-%{version}-root

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
pe�nej jako�ci CD wymagany jest sliny procesor (Pentium, SPARCstation10, DEC
Alpha lub podobny). Ni�sz� jako�� (22 lub 11 kHz) mo�na uzyska� ju� na
procesorach 486.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%ifarch i386 i586 i686
make linux
%else
make linux-%{_target_cpu}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	BUGS COPYING CHANGES JUKEBOX README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,COPYING,CHANGES,JUKEBOX,README}.gz

%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Fri May 21 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [0.59q-1] 
- package is FHS 2.0 compliant,
- based on spec file written by Karsten Weiss <karsten@addx.au.s.shuttle.de>,
  modified for PLD use by me and Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>,
- pl translation by Marek Obuchowicz <elephant@shadow.eu.org>.  
