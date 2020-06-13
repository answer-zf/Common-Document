$(function () {
    var pagewin = $(window).width()
    var pagehei = $(window).height()
    $('body,.main,.page').css({ width: pagewin }).css({ height: pagehei })
    var len = $('.page').length
    var num = 0 //在哪页
    var numjia = 0 //重要必须有的。。防止多次滚动事件发生/*每次滚动鼠标时都是很“凶残”的一下子滚动很大一个幅度，而不是一小格一小格的慢慢滚动，这就导致了滚动的时候会多次触发onmousewheel事件，*/
    var done = true /*重要必须有的。。做个变量 var done=true ,scrollFunc事件里第一步就判断done为true时继续运行,否则跳出.animate之前或之后done=false(从此,事件无效)
    animate增加一个callback,使done=true(也就是动画结束,事件会继续有效)。也就是不写done那么scrollFunc事件只会执行一次。*/
    for (var i = 0; i < len; i++) {
        $('.pagination').append('<li></li>')
    }
    $('.pagination').find('li').eq(0).addClass('active')
    $('.pagination li').click(function () {
        num = $(this).index()
        $('.main')
            .stop()
            .animate({ marginTop: -num * pagehei }, 1000)
        $('.pagination')
            .find('li')
            .eq(num)
            .addClass('active')
            .siblings()
            .removeClass('active')
    })
    function xia() {
        if (num < len - 1 && done) {
            //不在最后一页的时候
            num++
            numjia++
            done = false
            if (numjia == 1) {
                //只有在滚轮滚动一次时才执行下面的。
                $('.main')
                    .stop()
                    .animate({ marginTop: -num * pagehei }, 1000, function () {
                        done = true
                        numjia = 0
                    })
            }
        } else if (done) {
            //在最后一页的时候
            num = 0
            numjia++
            done = false
            if (numjia == 1) {
                //只有在滚轮滚动一次时才执行下面的。
                $('.main')
                    .stop()
                    .animate({ marginTop: -num * pagehei }, 1000, function () {
                        done = true
                        numjia = 0
                    })
            }
        }
    }
    function shang() {
        if (num > 0 && done) {
            //不在第一页的时候
            num--
            numjia++
            done = false
            if (numjia == 1) {
                //只有在滚轮滚动一次时才执行下面的。
                $('.main')
                    .stop()
                    .animate({ marginTop: -num * pagehei }, 1000, function () {
                        done = true
                        numjia = 0
                    })
            }
        } else if (done) {
            //在第一页的时候
            num = len - 1
            numjia++
            done = false
            if (numjia == 1) {
                //只有在滚轮滚动一次时才执行下面的。
                $('.main')
                    .stop()
                    .animate({ marginTop: -num * pagehei }, 1000, function () {
                        done = true
                        numjia = 0
                    })
            }
        }
    }
    function scrollFunc(e) {
        e = e || window.event //给e赋值event对象
        if (e.wheelDelta) {
            //IE/Opera/Chrome 情况时执行
            if (e.wheelDelta <= -120) {
                //判断滚轮是否下滚
                xia()
            } else if (e.wheelDelta >= 120) {
                //判断滚轮是否往上滚动
                shang()
            }
        } else if (e.detail) {
            //火狐 情况时执行
            if (e.detail >= 3) {
                //滚轮往下滚动时
                xia()
            } else if (e.detail <= -3) {
                //判断滚轮是否往上滚动
                shang()
            }
        }
        $('.pagination')
            .find('li')
            .eq(num)
            .addClass('active')
            .siblings()
            .removeClass('active')
    }
    //注册事件
    if (document.addEventListener) {
        document.addEventListener('DOMMouseScroll', scrollFunc, false)
    } //火狐浏览的事件绑定方式
    window.onmousewheel = document.onmousewheel = scrollFunc //其他浏览器绑定事件方式 如IE/Opera/Chrome
})
