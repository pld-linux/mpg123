#
# Conditional build:
%bcond_with	mmx	# use MMX to decode stream (won't run without MMX)
%bcond_without	esd	# don't build esound subpackage
#
Summary:	MPEG audio player
Summary(es):	Ejecuta archivos MP3
Summary(pl):	Odtwarzacz plik�w audio MPEG
Summary(pt_BR):	Tocador de arquivos MP3
Summary(ru):	������������� MPEG �����������
Summary(uk):	��������� MPEG ��Ħ����̦�
Name:		mpg123
Version:	0.59s
Release:	0.pre.9
Group:		Applications/Sound
License:	freely distributable for non-commercial use, GPL (mpglib)
Source0:	http://www.mpg123.de/mpg123/%{name}-pre%{version}.tar.gz
# Source0-md5:	a63675b0ea7990d4a7d7e7e14f23a3e4
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-esd.patch
Patch2:		%{name}-audio_sun.patch
Patch3:		%{name}-security.patch
Patch4:		%{name}-id3v2-hack.patch
Patch5:		%{name}-http-overflow.patch
Patch6:		%{name}-layer2-overflow.patch
Patch7:		%{name}-bufoverflow.patch
Patch8:		%{name}-CAN-2004-1284.patch
URL:		http://www.mpg123.de/
%{?with_esd:BuildRequires:	esound-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch %{ix86}
%ifarch athlon
%define		trgt	linux-3dnow
%else
%ifarch i586 i686
%define		trgt	linux%{?with_mmx:-mmx}
%else
%define		trgt	linux-i486
%endif
%endif
%else
%ifarch %{x8664}
%define		trgt	linux-amd64
%else
%define		trgt	linux-%{_target_cpu}
%endif
%endif

%define		specflags	-fomit-frame-pointer

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
Mpg123 jest szybkim, darmowym (do cel�w niekomercyjnych) oraz
uniwersalnym dekoderem plik�w d�wi�kowych MPEG dla system�w
uniksowych. Obs�uguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(s�ynne "MP3"). Do uzyskania pe�nej jako�ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni�sz�
jako�� (22 lub 11 kHz) mo�na uzyska� ju� na procesorach i486.

%description -l pt_BR
O mpg123 � um tocador de �udio MPEG para o Unix. Ele suporta MPEG
1.0/2.0 camadas 1, 2 e 3 (Arquivos "MP3").

%description -l ru
Mpg123 - ��� �������, ��������� � ����������� ������������� MPEG
�����������. �� ������������ MPEG 1.0/2.0 ������� 1, 2 � 3 ("MP3"
�����). ��� ��������� �������� �������� �������-����� (44 kHz, 16 ���,
������) ���������� ��������� Pentium. �������� ��� ���� �������
�������� (22 kHz ��� 11 kHz) �������� � �� ����������� ������ i486.

%description -l uk
Mpg123 - �� �������, צ����� �� ����������� ��������� MPEG
��Ħ����̦�. ��� Ц�����դ MPEG 1.0/2.0 Ҧ�Φ� 1, 2 �� 3 ("MP3"
�����). ��� ��������� ����Ԧ �������� �������-����� (44 kHz, 16 ¦�,
������) ����Ȧ���� �������� Pentium. �������� �� ���� Ǧ��ϧ ����Ԧ
(22 kHz �� 11 kHz) �������� � �� ���������� ����� i486.

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
Mpg123 jest szybkim, darmowym (do cel�w niekomercyjnych) oraz
uniwersalnym dekoderem plik�w d�wi�kowych MPEG dla system�w
uniksowych. Obs�uguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(s�ynne "MP3"). Do uzyskania pe�nej jako�ci CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Ni�sz�
jako�� (22 lub 11 kHz) mo�na uzyska� ju� na procesorach 486.

Wersja z wyj�ciem na ESD.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p1
%patch8 -p1

%build
%{__make} %{trgt} \
	OPT_FLAGS="%{rpmcflags} -DINET6"

mv -f mpg123 mpg123.base
%if %{with esd}
%{__make} clean
%{__make} %{trgt}-esd \
	OPT_FLAGS="%{rpmcflags} -DINET6"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name}.base	$RPM_BUILD_ROOT%{_bindir}/%{name}
%if %{with esd}
install %{name}		$RPM_BUILD_ROOT%{_bindir}/%{name}-esd
%endif
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BENCHMARKING BUGS CHANGES COPYING JUKEBOX README README.remote TODO
%ifarch athlon
%doc README.3DNOW
%endif
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*

%if %{with esd}
%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-esd
%endif