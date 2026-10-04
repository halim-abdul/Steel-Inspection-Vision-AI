subroutine ewma(x,n,alpha,y)
  implicit none
  integer, intent(in) :: n
  real(8), intent(in) :: x(n), alpha
  real(8), intent(out) :: y(n)
  integer :: i
  y(1)=x(1)
  do i=2,n
     y(i)=alpha*x(i)+(1.0d0-alpha)*y(i-1)
  end do
end subroutine ewma
