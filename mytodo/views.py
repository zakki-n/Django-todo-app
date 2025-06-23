from django.shortcuts import render
from django.views import View # クラスベースビューを継承するのに必要
from .models import Task 
from .forms import TaskForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

class IndexView(View):
    def get(self, request):
        incomplete_tasks = Task.objects.filter(complete=False).order_by('start_date')
        
        complete_tasks = Task.objects.filter(complete=True).order_by('start_date')
        todo_list = list(incomplete_tasks) + list(complete_tasks)
        
        context = {"todo_list": todo_list}
        return render(request, "mytodo/index.html", context)

    
class AddView(View):
    def get(self, request):
        #からのフォームを作ってテンプレートに返す
        form = TaskForm()
        # テンプレートのレンダリング処理
        return render(request, "mytodo/add.html" , {'form': form})

    def post(self, request, *args, **kwargs):
        # 登録処理
        # 入力データをフォームに渡す
        form = TaskForm(request.POST)
        # 入力データに誤りがないかチェック
        is_valid = form.is_valid()

        # データが正常であれば
        if is_valid:
            # モデルに登録
            form.save()
            return redirect('/')

        # データが正常じゃない
        return render(request, 'mytodo/add.html', {'form': form})
    
class Update_task_complete(View):
        def post(self, request, *args, **kwargs):
            task_id = request.POST.get('task_id')
            task = Task.objects.get(id=task_id)
            task.complete = not task.complete
            task.save()
            return redirect('/')
        
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)

    return render(request, 'mytodo/edit.html', {'form': form, 'task': task})
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')

# ビュークラスをインスタンス化
index = IndexView.as_view()
add = AddView.as_view()
update_task_complete = Update_task_complete.as_view()
