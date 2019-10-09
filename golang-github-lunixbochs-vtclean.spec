# Generated by go2rpm 1
%bcond_without check

# https://github.com/lunixbochs/vtclean
%global goipath         github.com/lunixbochs/vtclean
Version:                1.0.0

%gometa

%global common_description %{expand:
Clean up raw terminal output by stripping escape sequences, optionally
preserving color.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Strips terminal escapes from text, can preserve color

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in vtclean; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Oct 05 05:00:48 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.0-1
- Initial package

