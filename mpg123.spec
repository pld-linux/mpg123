#
# TODO: check why SDL still doesn't work :/
#
# Conditional build:
%bcond_with	mmx	# use MMX to decode stream (won't run without MMX)
%bcond_without	esd	# disable esound supprot
%bcond_without	alsa	# disable alsa support
%bcond_without	jack	# disable jack support
%bcond_without	nas	# diasble nas support
%bcond_without	sdl	# disable sdl support
#
%ifarch pentium3 pentium4 athlon
%define		with_mmx	1
%endif
Summary:	MPEG audio player
Summary(es):	Ejecuta archivos MP3
Summary(pl):	Odtwarzacz plików audio MPEG
Summary(pt_BR):	Tocador de arquivos MP3
Summary(ru):	ğÒÏÉÇÒÙ×ÁÔÅÌØ MPEG ÁÕÄÉÏÆÁÊÌÏ×
Summary(uk):	ğÒÏÇÒÁ×ÁŞ MPEG ÁÕÄ¦ÏÆÁÊÌ¦×
Name:		mpg123
Version:	0.61
Release:	1
License:	LGPL, GPL (mpglib)
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/mpg123/%{name}-%{version}.tar.bz2
# Source0-md5:	13b505ec04e5afb10399c89f24e99f0e
Patch0:		%{name}-audio_nas.patch
Patch1:		%{name}-audio_sdl.patch
URL:		http://www.mpg123.de/
%{?with_sdl:BuildRequires:	SDL-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_esd:BuildRequires:	esound-devel}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on i486 CPUs.

%description -l es
Ejecuta archivos MP3.

%description -l pl
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików d¼wiêkowych MPEG dla systemów
uniksowych. Obs³uguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(s³ynne "MP3"). Do uzyskania pe³nej jako¶ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni¿sz±
jako¶æ (22 lub 11 kHz) mo¿na uzyskaæ ju¿ na procesorach i486.

%description -l pt_BR
O mpg123 é um tocador de áudio MPEG para o Unix. Ele suporta MPEG
1.0/2.0 camadas 1, 2 e 3 (Arquivos "MP3").

%description -l ru
Mpg123 - ÜÔÏ ÂÙÓÔÒÙÊ, Ó×ÏÂÏÄÎÙÊ É ĞÅÒÅÎÏÓÉÍÙÊ ĞÒÏÉÇÒÙ×ÁÔÅÌØ MPEG
ÁÕÄÉÏÆÁÊÌÏ×. ÏÎ ĞÏÄÄÅÒÖÉ×ÁÅÔ MPEG 1.0/2.0 ÕÒÏ×ÎÅÊ 1, 2 É 3 ("MP3"
ÆÁÊÌÙ). äÌÑ ĞÏÌÕŞÅÎÉÑ ËÁŞÅÓÔ×Á Ú×ÕŞÁÎÉÑ ËÏÍĞÁËÔ-ÄÉÓËÁ (44 kHz, 16 ÂÉÔ,
ÓÔÅÒÅÏ) ÎÏÅÏÂÈÏÄÉÍ ĞÒÏÃÅÓÓÏÒ Pentium. íÏÎÏÚ×ÕË ÉÌÉ Ú×ÕË ÈÕÄÛÅÇÏ
ËÁŞÅÓÔ×Á (22 kHz ÉÌÉ 11 kHz) ×ÏÚÍÏÖÅÎ É ÎÁ ĞÒÏÃÅÓÓÏÒÁÈ ËÌÁÓÓÁ i486.

%description -l uk
Mpg123 - ÃÅ Û×ÉÄËÉÊ, ×¦ÌØÎÉÊ ÔÁ ĞÅÒÅÎÏÓÉÍÉÊ ĞÒÏÇÒÁ×ÁŞ MPEG
ÁÕÄ¦ÏÆÁÊÌ¦×. ÷¦Î Ğ¦ÄÔÒÉÍÕ¤ MPEG 1.0/2.0 Ò¦×Î¦× 1, 2 ÔÁ 3 ("MP3"
ÆÁÊÌÉ). äÌÑ ÏÔÒÉÍÁÎÎÑ ÑËÏÓÔ¦ Ú×ÕŞÁÎÎÑ ËÏÍĞÁËÔ-ÄÉÓËÕ (44 kHz, 16 Â¦Ô,
ÓÔÅÒÅÏ) ÎÅÏÂÈ¦ÄÎÉÊ ĞÒÏÃÅÓÏÒ Pentium. íÏÎÏÚ×ÕË ŞÉ Ú×ÕË Ç¦ÒÛÏ§ ÑËÏÓÔ¦
(22 kHz ŞÉ 11 kHz) ÍÏÖÌÉ×ÉÊ ¦ ÎÁ ĞÒÏÃÅÓÏÒÁÈ ËÌÁÓÕ i486.

%package esd
Summary:	mpg123 for ESD
Summary(pl):	mpg123 dla ESD
Group:		Applications/Sound

%description esd
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for ESD audio output.

%description esd -l pl
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików d¼wiêkowych MPEG dla systemów
uniksowych. Obs³uguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(s³ynne "MP3"). Do uzyskania pe³nej jako¶ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni¿sz±
jako¶æ (22 lub 11 kHz) mo¿na uzyskaæ ju¿ na procesorach 486.

Wersja z wyj¶ciem d¼wiêku przez ESD.

%package alsa
Summary:	mpg123 for ALSA
Summary(pl):	mpg123 dla ALSA
Group:		Applications/Sound

%description alsa
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for ALSA audio output.

%description alsa -l pl
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików d¼wiêkowych MPEG dla systemów
uniksowych. Obs³uguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(s³ynne "MP3"). Do uzyskania pe³nej jako¶ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni¿sz±
jako¶æ (22 lub 11 kHz) mo¿na uzyskaæ ju¿ na procesorach 486.

Wersja z wyj¶ciem d¼wiêku ALSA.

%package jack
Summary:	mpg123 for JACK
Summary(pl):	mpg123 dla JACK
Group:		Applications/Sound

%description jack
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for JACK audio output.

%description jack -l pl
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików d¼wiêkowych MPEG dla systemów
uniksowych. Obs³uguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(s³ynne "MP3"). Do uzyskania pe³nej jako¶ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni¿sz±
jako¶æ (22 lub 11 kHz) mo¿na uzyskaæ ju¿ na procesorach 486.

Wersja z wyj¶ciem d¼wiêku przez JACK.

%package nas
Summary:	mpg123 for NAS
Summary(pl):	mpg123 dla NAS
Group:		Applications/Sound

%description nas
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for NAS audio output.

%description nas -l pl
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików d¼wiêkowych MPEG dla systemów
uniksowych. Obs³uguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(s³ynne "MP3"). Do uzyskania pe³nej jako¶ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni¿sz±
jako¶æ (22 lub 11 kHz) mo¿na uzyskaæ ju¿ na procesorach 486.

Wersja z wyj¶ciem d¼wiêku przez NAS.

%package sdl
Summary:	mpg123 for SDL
Summary(pl):	mpg123 dla SDL
Group:		Applications/Sound

%description sdl
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for SDL output.

%description sdl -l pl
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików d¼wiêkowych MPEG dla systemów
uniksowych. Obs³uguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(s³ynne "MP3"). Do uzyskania pe³nej jako¶ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni¿sz±
jako¶æ (22 lub 11 kHz) mo¿na uzyskaæ ju¿ na procesorach 486.

Wersja z wyj¶ciem d¼wiêku przez SDL.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-audio=oss \
	%{?with_mmx:--with-cpu=mmx}
%{__make}
mv -f src/mpg123 src/mpg123.base

%if %{with alsa}
%{__make} clean
%configure \
	%{?with_alsa:--with-audio=alsa} \
	%{?with_mmx:--with-cpu=mmx}
%{__make}
mv -f src/mpg123 src/mpg123-alsa
%endif

%if %{with esd}
%{__make} clean
%configure \
	%{?with_esd:--with-audio=esd} \
	%{?with_mmx:--with-cpu=mmx}
%{__make}
mv -f src/mpg123 src/mpg123-esd
%endif

%if %{with jack}
%{__make} clean
%configure \
	%{?with_jack:--with-audio=jack} \
	%{?with_mmx:--with-cpu=mmx}
%{__make}
mv -f src/mpg123 src/mpg123-jack
%endif

%if %{with nas}
%{__make} clean
%configure \
	%{?with_nas:--with-audio=nas} \
	%{?with_mmx:--with-cpu=mmx}
%{__make}
mv -f src/mpg123 src/mpg123-nas
%endif

%if %{with sdl}
%{__make} clean
%configure \
	%{?with_sdl:--with-audio=sdl} \
	%{?with_mmx:--with-cpu=mmx}
%{__make} \
	LDFLAGS="%{rpmldflags} -lSDL"
mv -f src/mpg123 src/mpg123-sdl
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install src/%{name}.base	$RPM_BUILD_ROOT%{_bindir}/%{name}

%if %{with alsa}
install src/%{name}-alsa		$RPM_BUILD_ROOT%{_bindir}/
%endif

%if %{with esd}
install src/%{name}-esd		$RPM_BUILD_ROOT%{_bindir}/
%endif

%if %{with jack}
install src/%{name}-jack	$RPM_BUILD_ROOT%{_bindir}/
%endif

%if %{with nas}
install src/%{name}-nas		$RPM_BUILD_ROOT%{_bindir}/
%endif

%if %{with sdl}
install src/%{name}-sdl		$RPM_BUILD_ROOT%{_bindir}/
%endif

install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/BENCHMARKING doc/BUGS ChangeLog README doc/README.remote doc/TODO
%ifarch athlon
%doc doc/README.3DNOW
%endif
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-alsa
%endif

%if %{with esd}
%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-esd
%endif

%if %{with jack}
%files jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-jack
%endif

%if %{with nas}
%files nas
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-nas
%endif

%if %{with sdl}
%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-sdl
%endif
