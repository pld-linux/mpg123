Summary:	MPEG audio player
Summary(pl):	Odtwarzacz plików audio MPEG
Name:		mpg123
Version:	0.59r
Release:	3
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Copyright:	Freely distributable for non-commercial use
Source0:	http://www.mpg123.de/mpg123/%{name}-%{version}.tar.gz
Patch0:		ftp://ftp.kame.net/pub/kame/misc/mpg123-059r-v6-20000111.diff.gz
Patch1:		mpg123-makefile.patch
URL:		http://www.mpg123.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mpg123 is a fast, free(for non-commercial use) and portable MPEG audio
player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3 (those
famous "mp3" files). For full CD quality playback (44 kHz, 16 bit,
stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

%description -l pl
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików d¼wiêkowych MPEG dla systemów unixowych.
Obs³uguje standart MPEG 1.0/2.0 warstwy 1, 2 oraz 3 (s³ynne "mp3"). Do
uzyskania pe³nej jako¶ci CD wymagany jest silny procesor (Pentium,
SPARCstation10, DEC Alpha lub podobny). Ni¿sz± jako¶æ (22 lub 11 kHz)
mo¿na uzyskaæ ju¿ na procesorach 486.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .wiget

%build
%ifarch i386 i586 i686
%{__make} OPT_FLAGS="$RPM_OPT_FLAGS -DINET6" linux 
%else
%{__make} OPT_FLAGS="$RPM_OPT_FLAGS -DINET6" linux-%{_target_cpu}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s %{name} $RPM_BUILD_ROOT%{_bindir}
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
