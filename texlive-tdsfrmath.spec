Name:		texlive-tdsfrmath
Version:	15878
Release:	2
Summary:	Macros for French teachers of mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tdsfrmath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdsfrmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdsfrmath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdsfrmath.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of macros for French maths teachers in colleges
and lycees (and perhaps elsewhere). It is hoped that the
package will facilitate the everyday use of LaTeX by
mathematics teachers.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tdsfrmath/suite.sto
%{_texmfdistdir}/tex/latex/tdsfrmath/taupe.sto
%{_texmfdistdir}/tex/latex/tdsfrmath/tdsfrmath.sty
%doc %{_texmfdistdir}/doc/latex/tdsfrmath/LISEZMOI
%doc %{_texmfdistdir}/doc/latex/tdsfrmath/README
%doc %{_texmfdistdir}/doc/latex/tdsfrmath/tdsfrmath.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tdsfrmath/Makefile
%doc %{_texmfdistdir}/source/latex/tdsfrmath/tdsfrmath.dtx
%doc %{_texmfdistdir}/source/latex/tdsfrmath/tdsfrmath.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
