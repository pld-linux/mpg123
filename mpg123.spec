#
# Conditional build:
%bcond_with	mmx	# use MMX to decode stream (won't run without MMX)
%bcond_without	esd	# disable esound supprot
%bcond_without	alsa	# disable alsa support
%bcond_without	jack	# disable jack support
%bcond_with	sdl	# disable sdl support
#
Summary:	MPEG audio player
Summary(es):	Ejecuta archivos MP3
Summary(pl):	Odtwarzacz plikСw audio MPEG
Summary(pt_BR):	Tocador de arquivos MP3
Summary(ru):	Проигрыватель MPEG аудиофайлов
Summary(uk):	Програвач MPEG ауд╕офайл╕в
Name:		mpg123
Version:	0.61
Release:	0.1
License:	freely distributable for non-commercial use, GPL (mpglib)
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/mpg123/%{name}-%{version}.tar.bz2
# Source0-md5:	13b505ec04e5afb10399c89f24e99f0e
URL:		http://www.mpg123.de/
%{?with_sdl:BuildRequires:	SDL_sound-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_esd:BuildRequires:	esound-devel}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mpg123 is a fast, free(for non-commercial use) and portable MPEG audio
player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3 (those
famous "MP3" files). For full CD quality playback (44 kHz, 16 bit,
stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on i486 CPUs.

%description -l es
Ejecuta archivos MP3.

%description -l pl
Mpg123 jest szybkim, darmowym (do celСw niekomercyjnych) oraz
uniwersalnym dekoderem plikСw d╪wiЙkowych MPEG dla systemСw
uniksowych. ObsЁuguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(sЁynne "MP3"). Do uzyskania peЁnej jako╤ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni©sz╠
jako╤Ф (22 lub 11 kHz) mo©na uzyskaФ ju© na procesorach i486.

%description -l pt_BR
O mpg123 И um tocador de Аudio MPEG para o Unix. Ele suporta MPEG
1.0/2.0 camadas 1, 2 e 3 (Arquivos "MP3").

%description -l ru
Mpg123 - это быстрый, свободный и переносимый проигрыватель MPEG
аудиофайлов. он поддерживает MPEG 1.0/2.0 уровней 1, 2 и 3 ("MP3"
файлы). Для получения качества звучания компакт-диска (44 kHz, 16 бит,
стерео) ноеобходим процессор Pentium. Монозвук или звук худшего
качества (22 kHz или 11 kHz) возможен и на процессорах класса i486.

%description -l uk
Mpg123 - це швидкий, в╕льний та переносимий програвач MPEG
ауд╕офайл╕в. В╕н п╕дтриму╓ MPEG 1.0/2.0 р╕вн╕в 1, 2 та 3 ("MP3"
файли). Для отримання якост╕ звучання компакт-диску (44 kHz, 16 б╕т,
стерео) необх╕дний процесор Pentium. Монозвук чи звук г╕ршо╖ якост╕
(22 kHz чи 11 kHz) можливий ╕ на процесорах класу i486.

%package esd
Summary:	mpg123 for ESD
Summary(pl):	mpg123 dla ESD
Group:		Applications/Sound

%description esd
Mpg123 is a fast, free(for non-commercial use) and portable MPEG audio
player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3 (those
famous "MP3" files). For full CD quality playback (44 kHz, 16 bit,
stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for ESD output.

%description esd -l pl
Mpg123 jest szybkim, darmowym (do celСw niekomercyjnych) oraz
uniwersalnym dekoderem plikСw d╪wiЙkowych MPEG dla systemСw
uniksowych. ObsЁuguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(sЁynne "MP3"). Do uzyskania peЁnej jako╤ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni©sz╠
jako╤Ф (22 lub 11 kHz) mo©na uzyskaФ ju© na procesorach 486.

Wersja z wyj╤ciem na ESD.

%package alsa
Summary:	mpg123 for ALSA
Summary(pl):	mpg123 dla ALSA
Group:		Applications/Sound

%description alsa
Mpg123 is a fast, free(for non-commercial use) and portable MPEG audio
player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3 (those
famous "MP3" files). For full CD quality playback (44 kHz, 16 bit,
stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for ALSA output.

%description alsa -l pl
Mpg123 jest szybkim, darmowym (do celСw niekomercyjnych) oraz
uniwersalnym dekoderem plikСw d╪wiЙkowych MPEG dla systemСw
uniksowych. ObsЁuguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(sЁynne "MP3"). Do uzyskania peЁnej jako╤ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni©sz╠
jako╤Ф (22 lub 11 kHz) mo©na uzyskaФ ju© na procesorach 486.

Wersja z wyj╤ciem na ALSA.

%package jack
Summary:	mpg123 for Jack
Summary(pl):	mpg123 dla Jack
Group:		Applications/Sound

%description jack
Mpg123 is a fast, free(for non-commercial use) and portable MPEG audio
player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3 (those
famous "MP3" files). For full CD quality playback (44 kHz, 16 bit,
stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for Jack output.

%description jack -l pl
Mpg123 jest szybkim, darmowym (do celСw niekomercyjnych) oraz
uniwersalnym dekoderem plikСw d╪wiЙkowych MPEG dla systemСw
uniksowych. ObsЁuguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(sЁynne "MP3"). Do uzyskania peЁnej jako╤ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni©sz╠
jako╤Ф (22 lub 11 kHz) mo©na uzyskaФ ju© na procesorach 486.

Wersja z wyj╤ciem na Jack.

%package sdl
Summary:	mpg123 for SDL
Summary(pl):	mpg123 dla SDL
Group:		Applications/Sound

%description sdl
Mpg123 is a fast, free(for non-commercial use) and portable MPEG audio
player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3 (those
famous "MP3" files). For full CD quality playback (44 kHz, 16 bit,
stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for SDL output.

%description sdl -l pl
Mpg123 jest szybkim, darmowym (do celСw niekomercyjnych) oraz
uniwersalnym dekoderem plikСw d╪wiЙkowych MPEG dla systemСw
uniksowych. ObsЁuguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(sЁynne "MP3"). Do uzyskania peЁnej jako╤ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni©sz╠
jako╤Ф (22 lub 11 kHz) mo©na uzyskaФ ju© na procesorach 486.

Wersja z wyj╤ciem na SDL.

%prep
%setup -q

%build
%configure \
	%{?with_oss:--with-audio=oss} \
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

%if %{with sdl}
%{__make} clean
%configure \
	%{?with_sdl:--with-audio=sdl} \
	%{?with_mmx:--with-cpu=mmx}
%{__make}
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

%if %{with sdl}
%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-sdl
%endif
